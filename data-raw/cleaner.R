box::use(data.table[...])
box::use(dplyr[case_when])
box::use(stringr[str_to_lower])

clean_common <- function(col) {
  if (is.character(col)) {
    str_to_lower(col)
  } else if (is.numeric(col))  {
    round(col, 3)
  } else {
    col 
  }
}

read_all <- function(db, s3_url_map, s3_url_match, s3_url_player) {
  matches_raw <- (db$read_s3(s3_url_match))[stat_name != "NULL", lapply(.SD, clean_common)]
  maps_round <- (db$read_s3(s3_url_map))[, lapply(.SD, clean_common)]
  players <- (db$read_s3)(s3_url_player)[, lapply(.SD, clean_common)]
  list(matches_raw = matches_raw, 
       maps_round = maps_round,
       players = players)
}


clean_maps <- function(maps_round, matches_raw) {
  mtype <- unique(matches_raw[, .(map_type, map_name)])
  maps <- maps_round[mtype, on = "map_name"][
    , `:=`(attacker = NULL, defender = NULL)
  ]
  maps 
}

clean_player_info <- function(players, matches_raw) {
  player_info <- unique(matches_raw[, .(player_name, team_name)])[
    players, on = "player_name"
  ]
  player_info
}

clean_matches <- function(matches_raw) {
  matches <- matches_raw[,  .(
    match_id = esports_match_id, 
    date= as.IDate(start_time),
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
  player_info <- clean_player_info(data$players, data$matches_raw)
  matches <- clean_matches(data$matches_raw)
  player_stats <- clean_player_stats(matches)

  list(player_info = player_info, player_stats = player_stats, maps = maps, matches = matches)
}

