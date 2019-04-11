from big_ol_pile_of_manim_imports import *
import os
import pyclbr
import numpy as np
import random


class Together(GraphScene):

        CONFIG = {
            "x_min" : 0,
            "x_max" : 30,
            "y_min" : 0,
            "y_max" : 101,
            "y_tick_frequency": 5,
            "x_axis_label": None,
            "y_axis_label": None,
            "y_axis_height" : 5.7,
            "x_axis_width": 10,
            "graph_origin" : 3.4 * DOWN + 4 * LEFT,
            "function_color" : RED ,
            "axes_color" : GREEN,
            "x_labeled_nums" :range(0,100,10),
            "y_labeled_nums" :range(0,101,10)

        }
        def construct(self):
                    first_line=TextMobject("Sorting numbers is a fundamental ")
                    second_line=TextMobject("problem in computer science")
                    second_line.next_to(first_line,DOWN)
                    ##Extra set
                    EX_line1 = TextMobject("The most intuitive way of sorting")
                    EX_line1.next_to(second_line,UP)
                    EX_line2 = TextMobject("is by swapping elements one by one")
                    EX_line2.next_to(EX_line1,DOWN)
                    ##Set 2
                    third_line=TextMobject("But basic swapping algorithms cannot")
                    third_line.next_to(second_line,UP)
                    fourth_line=TextMobject("overcome the barrier set by inversions")
                    fourth_line.next_to(third_line,DOWN)
                    ## Set 3
                    third_line2=TextMobject("But basic swapping algorithms cannot")
                    third_line2.scale(0.8)
                    third_line2.to_corner(UP+LEFT)
                    fourth_line2=TextMobject("overcome the barrier set by inversions") #$O(n\log{}n)$
                    fourth_line2.scale(0.8)
                    fourth_line2.next_to(third_line2,DOWN)
                    #grid = NumberPlane()

                    self.add(first_line, second_line)
                    self.wait(2.7)
                    self.play(
                        Transform(first_line, EX_line1),
                        Transform(second_line,EX_line2)
                        )
                    self.wait(2.7)
                    self.play(
                        Transform(first_line, third_line),
                        Transform(second_line,fourth_line)
                        )
                    self.wait(2.7)
                    self.play(
                        Transform(first_line, third_line2),
                        Transform(second_line,fourth_line2)
                        )

                    self.setup_axes(animate=True)
                    func_graph=self.get_graph(self.func_to_graph,self.function_color)
                    func_graph2=self.get_graph(self.func_to_graph2)
                    graph_lab = self.get_graph_label(func_graph, label = "n^2",x_val = 7.71)
                    graph_lab2=self.get_graph_label(func_graph2,label = "nlog(n)", x_val=16,direction=UP*1.84)#, x_val=-10, direction=UP/2




                    self.play(
                        ShowCreation(func_graph, rate = 70),
                        )
                    self.play(ShowCreation(graph_lab),
                        )

                    fifth_line = TextMobject("The Heapsort algorithm")
                    fifth_line.scale(0.8)
                    fifth_line.to_corner(UP+RIGHT)
                    sixth_line = TextMobject("breaks this barrier")
                    sixth_line.scale(0.8)
                    sixth_line.next_to(fifth_line, DOWN)
                    self.play(ShowCreation(fifth_line), ShowCreation(sixth_line))
                    self.wait(1.5)
                    self.play(
                        ShowCreation(func_graph2, rate = 70),
                        ShowCreation(graph_lab2)
                        )
                    self.wait(2)

        def func_to_graph(self,x):
            return np.power(x,2)


        def func_to_graph2(self,x):
            if x<1:
                return x*0.1
            return x*np.log(x)

##################################################################################################################
class ArrayToHeap(Scene):

    def construct(self):
        square1 = Square()
        square1.scale(0.8)
        square1.move_to(LEFT*4)

        square2 = Square()
        square2.scale(0.8)
        square2.move_to(square1)

        square3 = Square()
        square3.scale(0.8)
        square3.move_to(square1)

        square4 = Square()
        square4.scale(0.8)
        square4.move_to(square1)

        square5 = Square()
        square5.scale(0.8)
        square5.move_to(square1)

        square6 = Square()
        square6.scale(0.8)
        square6.move_to(square1)

        square1N = Square()
        square1N.scale(0.8)
        square1N.move_to(square1)

        square2N = Square()
        square2N.scale(0.8)
        square2N.move_to(LEFT*2.4)

        square3N = Square()
        square3N.scale(0.8)
        square3N.move_to(LEFT*0.8)

        square4N = Square()
        square4N.scale(0.8)
        square4N.move_to(RIGHT*0.8)

        square5N = Square()
        square5N.scale(0.8)
        square5N.move_to(RIGHT*2.4)

        square6N = Square()
        square6N.scale(0.8)
        square6N.move_to(RIGHT*4)

        first_line = TextMobject("We are familiar with elements stored in an array")
        first_line.to_edge(UP)

        self.play(FadeIn(first_line))
        self.play(ShowCreation(square1))
        self.play(
                Transform(square2,square2N),
                Transform(square3,square3N),
                Transform(square4,square4N),
                Transform(square5,square5N),
                Transform(square6,square6N),
                )

        second_line = TextMobject("But viewing data in other ways")
        second_line.to_edge(UP)
        third_line = TextMobject("can show us new solutions to old problems")
        third_line.next_to(second_line,DOWN)

        self.wait()

        self.play(
            FadeOut(first_line)
            )
        self.play(
                Write(second_line),
                Write(third_line),
                rate = 0.1
        )

        self.wait(2)
        self.play(
            ApplyMethod(square1.move_to,DOWN*2+LEFT*4),
            ApplyMethod(square2.move_to,DOWN*2+LEFT*2.4),
            ApplyMethod(square3.move_to,DOWN*2+LEFT*0.8),
            ApplyMethod(square4.move_to,DOWN*2+RIGHT*0.8),
            ApplyMethod(square5.move_to,DOWN*2+RIGHT*2.4),
            ApplyMethod(square6.move_to,DOWN*2+RIGHT*4),
            rate = 20000
                )

        self.play(
                ApplyMethod(square1.set_color,BLUE),
                ApplyMethod(square2.set_color,RED),
                ApplyMethod(square3.set_color,RED),
                ApplyMethod(square4.set_color,GREEN),
                ApplyMethod(square5.set_color,GREEN),
                ApplyMethod(square6.set_color,GREEN),
                )

        self.play(
            ApplyMethod(square1.set_fill,BLUE, 0.1),
            ApplyMethod(square2.set_fill,RED,0.1),
            ApplyMethod(square3.set_fill,RED,0.1),
            ApplyMethod(square4.set_fill,GREEN,0.1),
            ApplyMethod(square5.set_fill,GREEN,0.1),
            ApplyMethod(square6.set_fill,GREEN,0.1),
            )



        circle1 = Circle(color = BLUE,fill_color = BLUE, fill_opacity=.1)
        circle1.scale(0.7)
        circle1.move_to(LEFT*3.8+UP*2.2)

        circle2 = Circle(color = RED)
        circle2.scale(0.7)
        circle2.move_to(LEFT*2+UP*0.3)

        circle3 = Circle(color = RED)
        circle3.scale(0.7)
        circle3.move_to(LEFT*0.2+UP*0.3)

        circle4 = Circle(color = GREEN)
        circle4.scale(0.7)
        circle4.move_to(RIGHT*0.2+DOWN*2)

        circle5 = Circle(color = GREEN)
        circle5.scale(0.7)
        circle5.move_to(RIGHT*2+DOWN*2)

        circle6 = Circle(color = GREEN)
        circle6.scale(0.7)
        circle6.move_to(RIGHT*3.8+DOWN*2)

        circleTemp = Circle(color=GREEN)
        circleTemp.scale(0.7)
        circleTemp.move_to(DOWN*2+RIGHT*3.3)



        fourth_line = TextMobject("Arrays can be viewed as a type of tree (heap)")
        fourth_line.to_edge(UP)

        self.play(
            Transform(third_line, fourth_line),
            FadeOut(second_line)
            )

        self.wait(1.5)

        self.play(
                Transform(square1, circle1),
                Transform(square2, circle2),
                Transform(square3, circle3),
                Transform(square4, circle4),
                Transform(square5, circle5),
                Transform(square6, circle6),
                )


        self.play(
            ApplyMethod(square1.move_to, UP*2.2),
            ApplyMethod(square2.move_to, LEFT*2+UP*0.3),
            ApplyMethod(square3.move_to, RIGHT*2+UP*0.3),
            ApplyMethod(square4.move_to, LEFT*3.2+DOWN*2),
            ApplyMethod(square5.move_to, LEFT*0.9+DOWN*2),
            ApplyMethod(square6.move_to, RIGHT*0.8+DOWN*2)
            )

        line1 = Line(square1,square2)
        line2 = Line(square1,square3)
        line3 = Line(square2,square4)
        line4 = Line(square2,square5)
        line5 = Line(square3,square6)
        line6 = Line(square3,circleTemp)

        self.play(
            ShowCreation(line1),
            ShowCreation(line2),
            ShowCreation(line3),
            ShowCreation(line4),
            ShowCreation(line5),
            )###############

        self.wait(1.8)

        ##################### ----- Heap explanation PART ---- ################################

        heapline1 = TextMobject("Heapsort uses a special type of tree")
        heapline1.to_edge(UP)
        self.play(
            Transform(third_line,heapline1),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3),
            FadeOut(line4),
            FadeOut(line5),
            FadeOutAndShiftDown(square1),
            FadeOutAndShiftDown(square2),
            FadeOutAndShiftDown(square3),
            FadeOutAndShiftDown(square4),
            FadeOutAndShiftDown(square5),
            FadeOutAndShiftDown(square6)
            )
        self.wait(1.8)
        heapline2 = TextMobject("A complete binary tree is filled from left to right")
        heapline2.to_edge(UP)
        self.play(Transform(third_line, heapline2))
        self.play(FadeIn(square1))
        self.play(FadeIn(square2),FadeIn(line1))
        self.play(FadeIn(square3),FadeIn(line2))
        self.play(FadeIn(square4),FadeIn(line3))
        self.play(FadeIn(square5),FadeIn(line4))
        self.play(FadeIn(square6),FadeIn(line5))
        self.play(FadeIn(circleTemp),FadeIn(line6))

        self.wait(1.9)
        ##################### ----- Extra Node ---- ################################

        heapline3 = TextMobject("All levels are required to be full")
        heapline3.to_edge(UP)
        self.play(Transform(third_line, heapline3))
        self.wait(1.5)
        heapline4 = TextMobject("Except the leaves, which do not have to be full")
        heapline4.to_edge(UP)
        self.play(Transform(third_line, heapline4))
        self.play(FadeOutAndShiftDown(circleTemp),FadeOutAndShiftDown(line6))
        self.wait(2)



        ##################### ----- SWAPPING PART ---- ########################################


        ########################SCALE##################

        circle1 = Circle(color = BLUE,fill_color = BLUE, fill_opacity=.1)
        circle1.scale(0.7*0.9)
        circle1.move_to(UP*2.2)

        circle2 = Circle(color = RED)
        circle2.scale(0.7*1.05)
        circle2.move_to(LEFT*2+UP*0.3)

        circle3 = Circle(color = RED)
        circle3.scale(0.7*1.2)
        circle3.move_to(RIGHT*2+UP*0.3)

        circle4 = Circle(color = GREEN)
        circle4.scale(0.7*1.25)
        circle4.move_to(LEFT*3.2+DOWN*2)

        circle5 = Circle(color = GREEN)
        circle5.scale(0.7)
        circle5.move_to(LEFT*0.9+DOWN*2)

        circle6 = Circle(color = GREEN)
        circle6.scale(0.7*0.6)
        circle6.move_to(RIGHT*0.8+DOWN*2)

        line1N = Line(circle1,circle2)
        line2N = Line(circle1,circle3)
        line3N = Line(circle2,circle4)
        line4N = Line(circle2,circle5)
        line5N = Line(circle3,circle6)

        scale_line = TextMobject("Trees can be used to sort elements of different sizes")
        scale_line.to_edge(UP)

        self.play(Transform(third_line, scale_line))

        self.play(
                Transform(square1, circle1),
                Transform(square2, circle2),
                Transform(square3, circle3),
                Transform(square4, circle4),
                Transform(square5, circle5),
                Transform(square6, circle6),
                Transform(line1, line1N),
                Transform(line2, line2N),
                Transform(line3, line3N),
                Transform(line4, line4N),
                Transform(line5, line5N)
                )

        self.wait(2)


        #############################SWAPPING###########################



        fifth_line = TextMobject("Changes in the tree translate to the array")
        fifth_line.to_edge(UP)

        self.wait()
        self.play(
            FadeOut(line5),
            FadeOut(line2),
            ApplyMethod(square3.move_to, RIGHT*1+DOWN*2),
            ApplyMethod(square6.move_to, RIGHT*2+UP*0.3),
            )
        line2 = Line(square6,square1)
        line5 = Line(square3,square6)
        self.play(FadeIn(line5),FadeIn(line2))

        self.play(
            FadeOut(line2),
            FadeOut(line5),
            FadeOut(line1),
            ApplyMethod(square6.move_to, UP*2.2),
            ApplyMethod(square1.move_to, RIGHT*2+UP*0.3),
            )
        line5 = Line(square1,square3)
        line2 = Line(square6,square1)
        line1 = Line(square6,square2)
        self.play(
            FadeIn(line2),
            FadeIn(line5),
            FadeIn(line1)
        )
        self.play(Transform(third_line,fifth_line))
        self.wait(1)
        #######################################


        self.play(
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3),
            FadeOut(line4),
            FadeOut(line5),
            ApplyMethod(square6.move_to, UP*2.2+LEFT*3.8),
            ApplyMethod(square2.move_to, LEFT*2+UP*0.3),
            ApplyMethod(square1.move_to, LEFT*0.2+UP*0.3),
            ApplyMethod(square4.move_to, RIGHT*0.2+DOWN*2),
            ApplyMethod(square5.move_to, RIGHT*2+DOWN*2),
            ApplyMethod(square3.move_to, RIGHT*3.8+DOWN*2)
            )

        square1N.move_to(DOWN*2+LEFT*4)
        square1N.set_color(GREEN)
        square1N.set_fill(GREEN,opacity=0.1)
        square2N.move_to(DOWN*2+LEFT*2.4)
        square2N.set_color(RED)
        square2N.set_fill(RED,opacity=0.1)
        square3N.move_to(DOWN*2+LEFT*0.8)
        square3N.set_color(BLUE)
        square3N.set_fill(BLUE,opacity=0.1)
        square4N.move_to(DOWN*2+RIGHT*0.8)
        square4N.set_color(GREEN)
        square4N.set_fill(GREEN,opacity=0.1)
        square5N.move_to(DOWN*2+RIGHT*2.4)
        square5N.set_color(GREEN)
        square5N.set_fill(GREEN,opacity=0.1)
        square6N.move_to(DOWN*2+RIGHT*4)
        square6N.set_color(RED)
        square6N.set_fill(RED,opacity=0.1)


        self.play(
            Transform(square6, square1N),
            Transform(square2, square2N),
            Transform(square1, square3N),
            Transform(square4, square4N),
            Transform(square5, square5N),
            Transform(square3, square6N)
            )
        self.play(
            ApplyMethod(square6.move_to,LEFT*4),
            ApplyMethod(square2.move_to,LEFT*2.4),
            ApplyMethod(square1.move_to,LEFT*0.8),
            ApplyMethod(square4.move_to,RIGHT*0.8),
            ApplyMethod(square5.move_to,RIGHT*2.4),
            ApplyMethod(square3.move_to,RIGHT*4)
            )
        self.wait(4)






##########################################################################################################
class SortedArray(Scene):
    def construct(self):
                square1 = Square()
                square1.scale(0.8)
                square1.move_to(LEFT*4+DOWN*2.5)

                square2 = Square()
                square2.scale(0.8)
                square2.move_to(square1)

                square3 = Square()
                square3.scale(0.8)
                square3.move_to(square1)

                square4 = Square()
                square4.scale(0.8)
                square4.move_to(square1)

                square5 = Square()
                square5.scale(0.8)
                square5.move_to(square1)

                square6 = Square()
                square6.scale(0.8)
                square6.move_to(square1)

                square1N = Square()
                square1N.scale(0.8)
                square1N.move_to(square1)

                square2N = Square()
                square2N.scale(0.8)
                square2N.move_to(LEFT*2.4+DOWN*2.5)

                square3N = Square()
                square3N.scale(0.8)
                square3N.move_to(LEFT*0.8+DOWN*2.5)

                square4N = Square()
                square4N.scale(0.8)
                square4N.move_to(RIGHT*0.8+DOWN*2.5)

                square5N = Square()
                square5N.scale(0.8)
                square5N.move_to(RIGHT*2.4+DOWN*2.5)

                square6N = Square()
                square6N.scale(0.8)
                square6N.move_to(RIGHT*4+DOWN*2.5)


                six=TextMobject("6")
                six.move_to(LEFT*4+DOWN*2.5)
                eight=TextMobject("8")
                eight.move_to(LEFT*2.4+DOWN*2.5)
                three=TextMobject("3")
                three.move_to(LEFT*0.8+DOWN*2.5)
                five=TextMobject("5")
                five.move_to(RIGHT*0.8+DOWN*2.5)
                four=TextMobject("4")
                four.move_to(RIGHT*2.4+DOWN*2.5)
                one=TextMobject("1")
                one.move_to(RIGHT*4+DOWN*2.5)

                sixN=TextMobject("6")
                sixN.move_to(LEFT*4+DOWN*2.5)
                eightN=TextMobject("8")
                eightN.move_to(LEFT*2.4+DOWN*2.5)
                threeN=TextMobject("3")
                threeN.move_to(LEFT*0.8+DOWN*2.5)
                fiveN=TextMobject("5")
                fiveN.move_to(RIGHT*0.8+DOWN*2.5)
                fourN=TextMobject("4")
                fourN.move_to(RIGHT*2.4+DOWN*2.5)
                oneN=TextMobject("1")
                oneN.move_to(RIGHT*4+DOWN*2.5)



                first_line = TextMobject("Let's look at an example")

                self.play(FadeIn(first_line))
                self.play(ShowCreation(square1))
                self.play(
                        Transform(square2,square2N),
                        Transform(square3,square3N),
                        Transform(square4,square4N),
                        Transform(square5,square5N),
                        Transform(square6,square6N),
                        )
                self.play(
                    Write(six),
                    Write(eight),
                    Write(three),
                    Write(five),
                    Write(four),
                    Write(one),
                    Write(sixN),
                    Write(eightN),
                    Write(threeN),
                    Write(fiveN),
                    Write(fourN),
                    Write(oneN),
                )

                circle1 = Circle(color = BLUE_E)
                circle1.scale(0.5)
                circle1.move_to(LEFT*3.8+UP*2.2)

                circle2 = Circle(color = BLUE_E)
                circle2.scale(0.5)
                circle2.move_to(LEFT*2+UP*0.6)

                circle3 = Circle(color = BLUE_E)
                circle3.scale(0.5)
                circle3.move_to(LEFT*0.2+UP*0.6)

                circle4 = Circle(color = BLUE_E)
                circle4.scale(0.5)
                circle4.move_to(RIGHT*0.2+DOWN*0.8)

                circle5 = Circle(color = BLUE_E)
                circle5.scale(0.5)
                circle5.move_to(RIGHT*2+DOWN*0.8)

                circle6 = Circle(color = BLUE_E)
                circle6.scale(0.5)
                circle6.move_to(RIGHT*3.8+DOWN*0.8)

                circleTemp = Circle(color=BLUE_E)
                circleTemp.scale(0.5)
                circleTemp.move_to(DOWN*0.8+RIGHT*3.1)



                second_line = TextMobject("What happens when these elements are sorted in a heap?")
                second_line.to_edge(UP)

                self.play(Transform(first_line,second_line))

                self.wait(1.5)

                self.play(
                        Transform(square1N, circle1),
                        ApplyMethod(sixN.move_to,LEFT*3.8+UP*2.2),
                        Transform(square2N, circle2),
                        ApplyMethod(eightN.move_to,LEFT*2+UP*0.6),
                        Transform(square3N, circle3),
                        ApplyMethod(threeN.move_to,LEFT*0.2+UP*0.6),
                        Transform(square4N, circle4),
                        ApplyMethod(fiveN.move_to,RIGHT*0.2+DOWN*0.8),
                        Transform(square5N, circle5),
                        ApplyMethod(fourN.move_to,RIGHT*2+DOWN*0.8),
                        Transform(square6N, circle6),
                        ApplyMethod(oneN.move_to,RIGHT*3.8+DOWN*0.8)
                        )


                self.play(
                    ApplyMethod(square1N.move_to, UP*2.2),
                    ApplyMethod(sixN.move_to,UP*2.2),
                    ApplyMethod(square2N.move_to, LEFT*1.8+UP*0.8),
                    ApplyMethod(eightN.move_to,LEFT*1.8+UP*0.8),
                    ApplyMethod(square3N.move_to, RIGHT*1.8+UP*0.8),
                    ApplyMethod(threeN.move_to,RIGHT*1.8+UP*0.8),
                    ApplyMethod(square4N.move_to, LEFT*3.2+DOWN*0.8), #############################
                    ApplyMethod(fiveN.move_to,LEFT*3.2+DOWN*0.8),
                    ApplyMethod(square5N.move_to, LEFT*0.9+DOWN*0.8),
                    ApplyMethod(fourN.move_to,LEFT*0.9+DOWN*0.8),
                    ApplyMethod(square6N.move_to, RIGHT*0.8+DOWN*0.8),
                    ApplyMethod(oneN.move_to,RIGHT*0.8+DOWN*0.8)
                    )

                self.wait(1.5)

                third_line = TextMobject("The heap is only logical. Everything happens in the array")
                third_line.to_edge(UP)

                self.play(Transform(first_line,third_line))
                self.wait(1.8)

################## 3 and 6 ##################
                self.play(
                    ApplyMethod(sixN.move_to,threeN),
                    ApplyMethod(square1N.move_to,square3N),
                    ApplyMethod(threeN.move_to,sixN),
                    ApplyMethod(square3N.move_to,square1N),
                    ApplyMethod(six.move_to,three),
                    ApplyMethod(three.move_to,six),
                )

################## 1 and 6 ##################

                self.play(
                    ApplyMethod(sixN.move_to,oneN),
                    ApplyMethod(square1N.move_to,square6N),
                    ApplyMethod(oneN.move_to,sixN),
                    ApplyMethod(square6N.move_to,square1N),
                    ApplyMethod(six.move_to,one),
                    ApplyMethod(one.move_to,six),
                )

################## 1 and 3 ##################

                self.play(
                    ApplyMethod(threeN.move_to,oneN),
                    ApplyMethod(square3N.move_to,square6N),
                    ApplyMethod(oneN.move_to,threeN),
                    ApplyMethod(square6N.move_to,square3N),
                    ApplyMethod(three.move_to,one),
                    ApplyMethod(one.move_to,three),
                )

################## 8 and 4 ##################

                self.play(
                    ApplyMethod(eightN.move_to,fourN),
                    ApplyMethod(square2N.move_to,square5N),
                    ApplyMethod(fourN.move_to,eightN),
                    ApplyMethod(square5N.move_to,square2N),
                    ApplyMethod(eight.move_to,four),
                    ApplyMethod(four.move_to,eight),
                )

################## EXPLANATION ##################
                fourth_line = TextMobject("This is a sorted heap. Each child is greater than its parent")
                fourth_line.to_edge(UP)
                self.play(Transform(first_line,fourth_line))

                line1 = Line(square1N,square3N)
                line2 = Line(square4N,square5N)
                line3 = Line(square5N,square6N)
                line4 = Line(square3N,square6N)
                line5 = Line(square2N,square5N)

                self.play(
                    FadeIn(line1),
                    FadeIn(line2),
                    FadeIn(line3),
                    FadeIn(line4),
                    FadeIn(line5)
                )

                self.wait(2.7)

                self.play(
                    FadeOut(line1),
                    FadeOut(line2),
                    FadeOut(line3),
                    FadeOut(line4),
                    FadeOut(line5)
                )

                new_line = TextMobject("But the array does not look sorted at first glance")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))

                self.play(
                    FadeOut(square1N),
                    FadeOut(sixN),
                    FadeOut(square2N),
                    FadeOut(eightN),
                    FadeOut(square3N),
                    FadeOut(threeN),
                    FadeOut(square4N),
                    FadeOut(fiveN),
                    FadeOut(square5N),
                    FadeOut(fourN),
                    FadeOut(square6N),
                    FadeOut(oneN),
                    ApplyMethod(square1.move_to,LEFT*4),
                    ApplyMethod(square2.move_to,LEFT*2.4),
                    ApplyMethod(square3.move_to,LEFT*0.8),
                    ApplyMethod(square4.move_to,RIGHT*0.8),
                    ApplyMethod(square5.move_to,RIGHT*2.4),
                    ApplyMethod(square6.move_to,RIGHT*4),
                    ApplyMethod(one.move_to,LEFT*4),
                    ApplyMethod(four.move_to,LEFT*2.4),
                    ApplyMethod(three.move_to,LEFT*0.8),
                    ApplyMethod(five.move_to,RIGHT*0.8),
                    ApplyMethod(eight.move_to,RIGHT*2.4),
                    ApplyMethod(six.move_to,RIGHT*4),
                )




                square1R = Square(color = GREEN, fill_color = GREEN, opacity = 0.2)
                square1R.scale(0.8)
                square1R.move_to(LEFT*4)

                square2R = Square(color = GREEN, fill_color = GREEN, opacity = 0.2)
                square2R.scale(0.8)
                square2R.move_to(LEFT*2.4)

                square3R = Square(color = GREEN, fill_color = GREEN, opacity = 0.2)
                square3R.scale(0.8)
                square3R.move_to(LEFT*0.8)

                square4R = Square(color = GREEN, fill_color = GREEN, opacity = 0.2)
                square4R.scale(0.8)
                square4R.move_to(RIGHT*0.8)

                square5R = Square(color = GREEN, fill_color = GREEN, opacity = 0.2)
                square5R.scale(0.8)
                square5R.move_to(RIGHT*2.4)

                square6R = Square(color = GREEN, fill_color = GREEN, opacity = 0.2)
                square6R.scale(0.8)
                square6R.move_to(RIGHT*4)

                self.wait(1.7)

#################### CREATING NEW ARRAY ###############################

                new_line = TextMobject("We would expect a sorted array to look like this")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))

                self.add(
                    square1R,
                    square2R,
                    square3R,
                    square4R,
                    square5R,
                    square6R,
                )


                self.play(
                    ApplyMethod(square1.move_to,LEFT*4+UP*1),
                    ApplyMethod(square2.move_to,LEFT*2.4+UP*1),
                    ApplyMethod(square3.move_to,LEFT*0.8+UP*1),
                    ApplyMethod(square4.move_to,RIGHT*0.8+UP*1),
                    ApplyMethod(square5.move_to,RIGHT*2.4+UP*1),
                    ApplyMethod(square6.move_to,RIGHT*4+UP*1),
                    ApplyMethod(one.move_to,LEFT*4+UP*1),
                    ApplyMethod(four.move_to,LEFT*2.4+UP*1),
                    ApplyMethod(three.move_to,LEFT*0.8+UP*1),
                    ApplyMethod(five.move_to,RIGHT*0.8+UP*1),
                    ApplyMethod(eight.move_to,RIGHT*2.4+UP*1),
                    ApplyMethod(six.move_to,RIGHT*4+UP*1),
                    ApplyMethod(square1R.move_to,LEFT*4+DOWN*1),
                    ApplyMethod(square2R.move_to,LEFT*2.4+DOWN*1),
                    ApplyMethod(square3R.move_to,LEFT*0.8+DOWN*1),
                    ApplyMethod(square4R.move_to,RIGHT*0.8+DOWN*1),
                    ApplyMethod(square5R.move_to,RIGHT*2.4+DOWN*1),
                    ApplyMethod(square6R.move_to,RIGHT*4+DOWN*1),
                    )



                sixR=TextMobject("6")
                eightR=TextMobject("8")
                threeR=TextMobject("3")
                fiveR=TextMobject("5")
                fourR=TextMobject("4")
                oneR=TextMobject("1")


                oneR.move_to(LEFT*4+UP*1)
                fourR.move_to(LEFT*2.4+UP*1)
                threeR.move_to(LEFT*0.8+UP*1)
                fiveR.move_to(RIGHT*0.8+UP*1)
                eightR.move_to(RIGHT*2.4+UP*1)
                sixR.move_to(RIGHT*4+UP*1)

                self.add(oneR,fourR,threeR,fiveR,eightR,sixR)

                self.play(
                     ApplyMethod(oneR.move_to,LEFT*4+ DOWN*1),
                     ApplyMethod(threeR.move_to,LEFT*2.4+ DOWN*1),
                     ApplyMethod(fourR.move_to,LEFT*0.8+ DOWN*1),
                     ApplyMethod(fiveR.move_to,RIGHT*0.8+ DOWN*1),
                     ApplyMethod(sixR.move_to,RIGHT*2.4+ DOWN*1),
                     ApplyMethod(eightR.move_to,RIGHT*4+ DOWN*1),
                )

                self.wait(2)

                new_line = TextMobject("In fact, both are sorted. Only with different logic")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))
################################# BACK TO TREE ############################

                self.play(
                    FadeOut(one),
                    FadeOut(three),
                    FadeOut(five),
                    FadeOut(four),
                    FadeOut(six),
                    FadeOut(eight),
                    FadeOut(oneR),
                    FadeOut(threeR),
                    FadeOut(fiveR),
                    FadeOut(fourR),
                    FadeOut(sixR),
                    FadeOut(eightR),
                    FadeOut(square1),
                    FadeOut(square2),
                    FadeOut(square3),
                    FadeOut(square4),
                    FadeOut(square5),
                    FadeOut(square6),
                    FadeOut(square1R),
                    FadeOut(square2R),
                    FadeOut(square3R),
                    FadeOut(square4R),
                    FadeOut(square5R),
                    FadeOut(square6R),
                )

                nineN = TextMobject("9")
                nineN.move_to(DOWN*0.8+RIGHT*3.3)
                self.play(
                    FadeIn(square1N),
                    FadeIn(square2N),
                    FadeIn(square3N),
                    FadeIn(square4N),
                    FadeIn(square5N),
                    FadeIn(square6N),
                    FadeIn(circleTemp),
                    FadeIn(oneN),
                    FadeIn(sixN),
                    FadeIn(threeN),
                    FadeIn(fourN),
                    FadeIn(fiveN),
                    FadeIn(eightN),
                    FadeIn(nineN),

                )

                self.wait()

                new_line = TextMobject("We can access elements in ascending order like this")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))

                self.wait()

                self.play(
                    ApplyMethod(square6N.move_to,LEFT*8+UP*8),
                    ApplyMethod(oneN.move_to,LEFT*8+UP*8),
                )

                new_line = TextMobject("We remove the root, move the last element to the top and sort")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))

                self.wait(2)

                self.play(
                    ApplyMethod(circleTemp.move_to,UP*2.2),
                    ApplyMethod(nineN.move_to,UP*2.2),
                )

################## 9 and 3 ##################

                self.play(
                    ApplyMethod(nineN.move_to,threeN),
                    ApplyMethod(circleTemp.move_to,square3N),
                    ApplyMethod(threeN.move_to,nineN),
                    ApplyMethod(square3N.move_to,circleTemp),
                )

################## 9 and 5 ##################

                self.play(
                    ApplyMethod(nineN.move_to,sixN),
                    ApplyMethod(circleTemp.move_to,square1N),
                    ApplyMethod(sixN.move_to,nineN),
                    ApplyMethod(square1N.move_to,circleTemp),
                )

                new_line = TextMobject("This function is recursive as we demonstrate below")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))

                self.wait(2.7)

                new_line = TextMobject("The worst case removal of all the elements is O(nlog(n))")
                new_line.to_edge(UP)
                self.play(Transform(first_line,new_line))

                self.wait(3)
#
