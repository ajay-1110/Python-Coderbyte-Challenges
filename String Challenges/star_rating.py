"""/****************************************************************
 *             CODERBYTE STAR RATING CHALLENGE                  *
 *                                                              *
 * Problem Statement                                            *
 * Have the function StarRating(str) take the str parameter     *
 * being passed which will be an average rating between         *
 * 0.00 and 5.00, and convert this rating into a list of 5 image*
 * names to be displayed in a user interface to represent the   *
 * rating as a list of stars and half stars. Ratings should be  *
 * rounded to the nearest half. There are 3 image file names    *
 * available: "full.jpg", "half.jpg", "empty.jpg".              *
 * The output will be the name of the 5 images                  *
 * (without the extension), from left to right, separated by    *
 * spaces.                                                      *
 *                                                              *
 * Examples                                                     *
 * Input 1: "0.38"                                              *
 * Output 1: half empty empty empty empty                       *
 *                                                              *
 * Input 2: "4.5"                                               *
 * Output 2: full full full full half                           *"""

def starrating(strn):
    x = float(strn)
    y = round(x*2)/2
    z = ""
    if int(y) == 0 and y/0.5 != 1:
        return "empty empty empty empty empty"
    if int(y) == 0 and y/0.5 == 1:
        return "half empty empty empty empty"
    if int(y) > 0:
        i = 0
        while i < int(y):
            z += "full "
            i += 1
        if (y - int(y))/0.5 != 1:
            for i in range(5 - int(y)):
                z += "empty "
        else:
            add = "half "
            for i in range(5 - int(y+1)):
                add += "empty "
            z += add
    return z.strip()


print(starrating("0.38"))
