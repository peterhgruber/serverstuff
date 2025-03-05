# short fibonacci
# peter.gruber@usi.ch, 2023-03-01

args <- commandArgs(trailingOnly=TRUE)

if (length(args) == 0) {
    stop("Please provide the number of elements to be calculated as an argument.")
}

fib <- c(1,1)
for (k in 3:args[1]) {fib[k] <- fib[k-1]+fib[k-2]}
fib
