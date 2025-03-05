# Download FX quotes and write to a CSV file
# Programming in Finance and Economics II
# peter.gruber@usi.ch, 2024-03

# To run, use
# Rscript fxday.R
# Then set up a cron job using
# crontab -e

require('quantmod')

USD<-getSymbols("EURUSD=X", auto.assign=F)
USD_latest <- tail(USD$`EURUSD=X.Close`,1)
FXdata <- data.frame(Sys.Date(),USD_latest)

write.table(FXdata,file='fx.csv', sep=",",
            row.names=F, col.names=F, append=T)




