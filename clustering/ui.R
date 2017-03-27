myData <- read.csv("quakes.csv", header=TRUE)
nums <- sapply(myData, is.numeric)

myData <- myData[,nums]

shinyUI(pageWithSidebar(
  headerPanel('k-means clustering'),
  
  sidebarPanel(
    selectInput('xcol', 'X Variable', names(myData)),
    selectInput('ycol', 'Y Variable', names(myData),
                selected=names(myData)[[2]]),
    numericInput('clusters', 'Cluster count', 3,
                 min = 1, max = 9)
  ),
  mainPanel(
    plotOutput('plot1'),
    textOutput('plot2'),
    textOutput('plot3')
  )
))