library(rvest)
library(stringr)
library(purrr)
library(dplyr)
library(lubridate)
library(paws)


url <- "https://liquipedia.net"

page <- read_html(paste0(url, "/overwatch/Players")) 

details_links <- page %>% 
  html_elements("#mw-content-text table tr td:nth-child(2) a") %>% 
  html_attr("href")

read_detail <- function(link) {
  detail_page <- read_html(paste0(url, link))

  cells_wrapper <- detail_page %>% 
    html_element(".infobox-ow") 
  
  game_id <- cells_wrapper %>% html_element(".infobox-header") %>% html_text()
  
  all_cols <- cells_wrapper %>%
    html_elements(xpath = ".//div[contains(@class, 'description')]") %>% 
    html_text2() %>% 
    str_remove_all(":") %>% 
    janitor::make_clean_names()
  
  all_values <- cells_wrapper %>%
    html_elements(xpath = ".//div[not(contains(@class, 'description'))]/*[@class='infobox-cell-2']") %>% 
    html_text2()
  
  
  l <- set_names(all_values, all_cols) %>% as.list()
  
  if (!is.null(l[["romanized_name"]])) {
    l$name2 <- l$romanized_name
  } else {
    l$name2 <- l$name
  }
  
  df <- tibble(
    player_name = game_id, 
    player_real_name = l$name2, 
    birth = l$birth, 
    country = l$country,
    status = l$status,
    team_name = l$team,
    earnings = l$approx_total_earnings,
    role = l$common_team_role_s,
    signature_hero = l$signature_hero
  )
  
  Sys.sleep(0.5)
  df 
}



players_raw <- map_dfr(details_links, read_detail)
readr::write_csv(players_raw, "scrapers/players_raw.csv")


players_clean <- players_raw %>% 
  mutate(player_name = str_remove_all(player_name, "\\[e]\\[h]") %>% str_squish(), 
        age = str_extract(birth, "(?<=age )\\d+"),
        birth = mdy(str_extract(birth, "\\w+ \\d{1,2}, \\d{4}")),
        earnings = readr::parse_number(earnings),
        signature_hero = str_replace_all(signature_hero, "Lúcio", "Lucio") %>% str_replace_all("Torbjörn", "Torbjoirn"))

readr::write_csv(players_clean, "scrapers/players_clean.csv")

s3_client <- s3()
s3_client$put_object(Body = "scrapers/players_clean.csv", Bucket = "owl-analysis", Key = "players/players_clean.csv")
