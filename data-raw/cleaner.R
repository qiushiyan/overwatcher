box::use(data.table[...])
box::use(dplyr[case_when])
box::use(stringr[str_to_lower])

clean_common <- function(col) {
  if (is.character(col)) {
    str_to_lower(col)
  } else if (is.numeric(col))  {
    round(col, 2)
  } else {
    col 
  }
}

read_all <- function(db, s3_url_map, s3_url_match, s3_url_player) {
  matches_raw <- (db$read_s3(s3_url_match))[stat_name != "NULL", lapply(.SD, clean_common)]
  maps_round <- (db$read_s3(s3_url_map))[, lapply(.SD, clean_common)]
  player_info <- (db$read_s3)(s3_url_player)[, lapply(.SD, clean_common)]
  list(matches_raw = matches_raw, 
       maps_round = maps_round,
       player_info = player_info)
}


clean_maps <- function(maps_round, matches_raw) {
  mtype <- unique(matches_raw[, .(map_type, map_name)])
  maps <- maps_round[mtype, on = "map_name"][
    , `:=`(match_date = max(as.IDate(round_start_time)),
          round_duration = round(as.numeric(round_end_time - round_start_time)/60, 1)), 
    match_id
  ][
    , `:=`(attacker = NULL, 
           defender = NULL, 
           round_start_time = NULL, 
           round_end_time = NULL)
  ][
    , `:=`(stage = case_when(
      stage == "overwatch league - stage 1" ~ "season1 stage1",
      stage == "overwatch league - stage 1 - title matches" ~ "season1 stage1 title",
      stage == "overwatch league - stage 2" ~ "season1 stage2",
      stage == "overwatch league - stage 2 - title matches" ~ "season1 stage2 title",
      stage == "overwatch league - stage 3" ~ "season1 stage3",
      stage == "overwatch league - stage 3 - title matches" ~ "season1 stage3 title",
      stage == "overwatch league - stage 4" ~ "season1 stage4",
      stage == "overwatch league - stage 4 - title matches" ~ "season1 stage4 title",
      stage == "overwatch league inaugural season championship" ~ "season1 playoff", 
      stage == "overwatch league stage 1" ~ "season2 stage1", 
      stage == "overwatch league stage 1 title matches" ~ "season2 stage1 title", 
      stage == "overwatch league stage 2" ~ "season2 stage2", 
      stage == "overwatch league stage 2 title matches" ~ "season2 stage2 title", 
      stage == "overwatch league stage 3" ~ "season2 stage3", 
      stage == "overwatch league stage 3 title matches" ~ "season2 stage3 title", 
      stage == "overwatch league stage 4" ~ "season2 stage4", 
      stage == "overwatch league 2019 post-season" ~ "season2 playoff", 
      stage == "owl 2020 regular season" ~ "season3", 
      stage == "owl 2021" ~ "season4",
      TRUE ~ NA_character_
    ))
  ][order(match_date)]
  maps 
}


clean_matches <- function(matches_raw) {
  matches <- matches_raw[,  .(
    match_id = esports_match_id, 
    date = as.IDate(start_time),
    tournament = tournament_title, 
    map_name,
    player_name,
    team_name, 
    hero_name = case_when(
      hero_name == "lúcio" ~ "lucio", 
      hero_name == "torbjörn" ~ "torbjorn", 
      TRUE ~ hero_name
    ),
    stat_name,
    stat_amount)
  ]
  
  matches 
}

clean_player_stats <- function(matches) {
  player_stats <- matches[
    , .(stat_mean = mean(stat_amount), count = .N),
    .(player_name, hero_name, map_name, stat_name)
  ]
  
  player_stats
}

#' @export 
clean_all <- function(db, s3_url_map, s3_url_match, s3_url_player) {
  data <- read_all(db, s3_url_map, s3_url_match, s3_url_player)
  
  maps <- clean_maps(data$maps_round, data$matches_raw)
  matches <- clean_matches(data$matches_raw)
  player_stats <- clean_player_stats(matches)

  list(player_info = data$player_info, player_stats = player_stats, maps = maps, matches = matches)
}

