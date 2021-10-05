box::use(./db[create_DB])
box::use(./cleaner)
box::use(conf = config)

box::reload(cleaner)

config <- conf$get()


DB <- create_DB()
db <- DB$new()

data <- cleaner$clean_all(db, 
                  s3_url_map = config$s3_url_map,
                  s3_url_match = config$s3_url_match,
                  s3_url_player = config$s3_url_player)

db$refresh_connection()
db$write_dt(data$player_info, "player_info")
db$write_dt(data$player_stats, "player_stats")
db$write_dt(data$maps, "maps")
db$write_dt(data$matches, "matches")


db$query("ALTER TABLE player_info MODIFY COLUMN birth DATE")
db$query("ALTER TABLE matches MODIFY COLUMN date DATE")
db$query("ALTER TABLE maps MODIFY COLUMN match_date DATE")

# build rmd 
box::use(rmarkdown[render])
render("readme.Rmd", output_file = "readme.md", output_dir = "..")
file.remove("../readme.html")
