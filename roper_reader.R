# Just source this right in
roper_reader = function(filename){
  
  substrRight <- function(x, n){
    substr(x, nchar(x)-n+1, nchar(x))
  }
  
  
  roper = read.csv(filename, sep = ";")
  r2 = sapply(X=1:nrow(roper), FUN = function(x) strsplit(as.character(roper[x,]), " ; "))

  text  = sapply(X=1:nrow(roper), FUN = function(x) r2[[x]][1])

  year_firm = sapply(X=1:nrow(roper), FUN = function(x) r2[[x]][2])
  yf2 = substr(year_firm, start=9, stop=nchar(year_firm))
  yf3 = strsplit(yf2, "\nInterview Dates:")

  y = sapply(X=1:nrow(roper), FUN = function(x) yf3[[x]][1])
  year = substrRight(y, 4)

  f = strsplit(y, ",")
  l = sapply(X=f, length)

  firm = c()
  for(i in 1:length(l)){
    if(l[i]==2){
      firm[i] = f[[i]][1]
    }
    if(l[i]!=2){
      firm[i] = paste(f[[i]][1:l[i]], f[[i]][2], collapse=" ")
    }
  }
  out = data.frame(cbind(text, firm, year))
  return(out)
}


files = sapply(X=1994:2013, FUN=function(x) paste("roper_", x, ".csv", sep=""))
out = lapply(X=files, FUN=roper_reader)

z = do.call("rbind", out)
save(z, file="roper_df.RData")


# actually do I maybe want to classify each year separately then rbind them?
# That requires having every classifier built...