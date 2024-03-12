box::use(DBI[dbConnect, dbGetQuery, dbWriteTable])
box::use(RPostgres[Postgres])
box::use(vroom[vroom])
box::use(R6[R6Class])
box::use(data.table[...])

#' @export
create_DB <- function() {
  R6Class("db connection",
    public = list(
      initialize = function() {
        private$con <- dbConnect(Postgres(),
          dbname = "overwatcher",
          host = Sys.getenv("OVERWATCHER_DB_HOST"),
          user = Sys.getenv("OVERWATCHER_DB_USER"),
          password = Sys.getenv("OVERWATCHER_DB_PASSWORD"),
          port = 5432)
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
