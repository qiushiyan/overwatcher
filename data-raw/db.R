box::use(DBI[dbConnect, dbGetQuery, dbWriteTable])
box::use(RMySQL[MySQL])
box::use(vroom[vroom])
box::use(R6[R6Class])
box::use(data.table[...])

#' @export
create_DB <- function() {
  R6Class("db connection to RDS", 
          public = list(
            initialize = function(dbname = "overwatcher", 
                                  host = "overwatcher.cnuwuhvikj0e.us-east-1.rds.amazonaws.com", 
                                  user = Sys.getenv("DB_OVERWATCHER_USER"),
                                  password = Sys.getenv("DB_OVERWATCHER_PASSWORD"), 
                                  port = 3306) {
              private$con <- dbConnect(MySQL(), 
                                       dbname = dbname,
                                       host = host, 
                                       user = user,
                                       password = password,
                                       port = port)
            }, 
            read_s3 = function(s3_url, name = NULL, n_max = Inf) {
              dt <- as.data.table(vroom(s3_url, n_max = n_max)) 
              rownames(dt) <- NULL 
              dt
            }, 
            write_dt = function(dt, table_name, overwrite = TRUE, row.names = FALSE) {
              dbWriteTable(private$con, table_name, dt, overwrite = overwrite, row.names = row.names)
            },
            query = function(statement) {
              as.data.table(dbGetQuery(private$con, statement))
            },
            refresh_connection = function() {
              self$initialize()
            }
          ),
          private = list(
            con = NULL 
          ))
}




