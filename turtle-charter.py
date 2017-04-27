import math
import random
import turtle

WIDTH=800
HEIGHT=500

def count_observations(datafile):
    """This function takes as input the data file and returns as output the number of data observations in the file"""
    linecount=0
    #count the number of lines in the file using a loop
    for line in datafile:
        linecount+=1
    #Divide the line count by 3 as each record takes 3 lines. Return the result
    return (int(linecount/3))

def get_max_value(datafile,feature):
    """This function takes as input the data file and the feature to analyze and returns the maximum value of the given feature"""
    #Taking the integer value of the feature number for which we want the max value
    feature_no=int(feature[-1])
    #declare a variable max to store the largest value of the feature. Initialize it to a very small number
    max=-99999
    for index,line in enumerate(datafile):
        if feature_no==1 and index%3==1:
            #If it is the first feature and we are at the line corresponding to the first feature
            if int(line)>max:
                #If the value of the data is greater than current max value, set max as current data value
                max=int(line)
        if feature_no==2 and index%3==2:
            #If it is the second feature and we are at the line corresponding to the second feature
            if int(line)>max:
                #If the value of the data is greater than current max value, set max as current data value
                max=int(line)  
    #Return the maximum value of given feature
    return max

def draw_x_axis(pointer):
    """This function takes as input the turtle object and draws the x axis on screen. No return value."""
    #draw a horizontal line at bottom of screen which represents the x axis
    pointer.forward(WIDTH-50)

def draw_y_axis(pointer):
    """This function takes as input the turtle object and draws the y axis on screen. no return value."""
    pointer.home()
    #draw a vertical line at left of screen which represents the y axis
    pointer.left(90)
    pointer.forward(HEIGHT)

def draw_y_tickmark(pointer,datafile):
    """This function takes as input the turtle object and the datafile and draws the y axis ticks on screen. No return value."""
    pointer.home()
    pointer.left(90)
    #Get the maximum value of data corresponding to the feature to be plotted
    maxval=get_max_value(datafile,'feature 1')
    #Divide the maximum value obtained by the length of each y axis division (7) to obtain number of ticks
    yhighest=math.ceil(maxval/7)
    #Draw the ticks and the corresponding numbers using a loop
    for y in range(yhighest):
        pointer.forward(50)
        pointer.left(90)
        pointer.forward(5)
        pointer.penup()
        pointer.forward(40)
        pointer.pendown()
        pointer.write((y+1)*7, font=("Arial", 8, "normal"))
        pointer.penup()
        pointer.left(180)
        pointer.forward(40)
        pointer.pendown()
        pointer.forward(5)
        pointer.left(90)

def draw_x_labels(pointer,datafile):
    """This function takes as input the turtle object and the datafile and draws the x axis labels on screen. No return value."""
    pointer.home()
    #Count the number of observations in the data file
    data_count=count_observations(datafile)
    #Use a loop to iterate over the data file and print out the labels on the x axis
    for i in range(data_count):
        #Select label value from file
        labelval=datafile[3*i]
        #Move to the location where the label needs to be printed
        pointer.forward(math.floor((WIDTH-100)/data_count))
        pointer.right(90)
        pointer.penup()
        pointer.forward(40)
        pointer.pendown()
        #print the label below the axis
        pointer.write(labelval, font=("Arial", 8, "normal"))
        pointer.penup()
        pointer.left(180)
        pointer.forward(40)
        pointer.right(90)
        pointer.pendown()
        
def choose_color():
    """This function when called returns a tuple of 3 values which are RGB values which can range from 0-255"""
    #Using the randint function to generate a tuple of 3 random numbers between 0-255 which correspond to RGB color values for each bar in the chart.
    return (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    
        
def draw_bars(pointer,datafile):
    """This function takes as input the turtle object and the datafile and draws all the bars of the barchart on screen. No return value."""
    pointer.home()
    #Count the observations in the file
    obs=count_observations(datafile)
    t=1
    #loop over the data file to draw the bars on the chart corresponding to the values of the feature
    for i in range(obs):
        #Select random color for current bar to be drawn
        color=choose_color()
        #Draw rectangle at specified position on the chart, with height proportionate to data value of the current feature value
        draw_rectangle(pointer,i*math.floor((WIDTH-100)/obs)+40,0,40,int(datafile[t]),color)
        t=t+3
        
def draw_rectangle(pointer,px,py,width,height,pen_color):
    """This function takes as input the turtle object, the x and y coordinates of the rectangle position, the width and height of the rectangle, the rectangle color, and draws the rectangle on screen. No return value."""
    pointer.penup()
    pointer.home()
    #Set position of bar
    pointer.setpos(px,py)
    pointer.pendown()
    #set the color of the pen
    pointer.color(pen_color)
    pointer.begin_fill()
    #draw a rectangle with the specified width and height
    for i in range(2):
        pointer.forward(width)
        pointer.left(90)
        pointer.forward(height*7)
        pointer.left(90)
    pointer.end_fill()

def turtleinit(datafile,viztitle):
    """This function takes as input the datafile and the bargraph title, initializes the turtle objects, creates the screen, and calls all the functions to create the bar graph. No return value."""
    #Initialize the screen
    wn=turtle.Screen()
    #Set the title of the bar graph
    wn.title(viztitle)
    #Set the width and height of window
    turtle.setup(width=WIDTH,height=HEIGHT,startx=0,starty=0)
    #Set the default position of the turtle pointer to be the bottom left and not centre
    turtle.setworldcoordinates(-100,-100,WIDTH,HEIGHT)
    #Set the color modes and speed of the turtle pointer
    turtle.colormode(255)
    turtle.speed(0)
    #Initialize a Turtle object to draw with
    pointer=turtle.Turtle()
    #Call the individual functions to plot the bar graph
    draw_x_axis(pointer)
    draw_y_axis(pointer)
    draw_y_tickmark(pointer,datafile)
    draw_x_labels(pointer,datafile)
    draw_bars(pointer,datafile)
    wn.mainloop()

def fileread():
    """This function takes the file path and title of the bar graph as inputs from the user, opens the data file, and calls the turtle init method to draw the visualization. No return value or funtion inputs."""
    #User input for file path
    file_path=input("Enter the path of the data file to visualize")
    #User input for title of the bar chart
    viztitle=input("Enter the title for the chart")
    #Open file and read the lines into a variable datafile
    f=open(file_path,mode='r')
    datafile=f.readlines()
    #call to the turtleinit function to draw the bar chart
    turtleinit(datafile,viztitle)

fileread()

if __name__ == "__main__":
    # execute only if run as a script
    main()