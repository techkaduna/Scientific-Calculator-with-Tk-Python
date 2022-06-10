import math
from tkinter import *
import logger



class Maths():
    def __init__(self,ent):
        self.ent = ent


    def sine(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.sin(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the sine operation')
        except:
            logger.logger.error('There was an error while doing the sine operation')

    def cosine(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.cos(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the cosine operation')
        except:
            logger.logger.error('There was an error while doing the cosine operation')    

    def tangent(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.tan(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the tangent operation')
        except:
            logger.logger.error('There was an error while doing the tangent operation')

    def sine_inv(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.asin(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the sine inverse operation')
        except Exception as e:
            logger.logger.error(e)

    def cos_inv(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.acos(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the cos-inverse operation')
        except Exception as e:
            logger.logger.error(e)

    def tan_inv(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.atan(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the tangent-inverse operation')
        except Exception as e:
            logger.logger.error(e)

    def log(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.log10(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the log10 operation')
        except:
            logger.logger.error('There was an error while doing the log10 operation')

    def lin(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.log(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the natural log operation')
        except Exception as e:
            logger.logger.error(e)

    def antiLog(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            #result = math.atan(x)
            #self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the antiLog operation// ....operation still pending')
        except Exception as e:
            logger.logger.error(e)

    def exponent(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(math.exp(x))
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the exponential operation')
        except:
            logger.logger.error('There was an error while doing the exponential operation')

    def degree(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(math.degrees(x))
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the degree conversion operation')
        except Exception as e:
            logger.logger.error(e)
        
    def radians(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(math.radians(x))
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the radians conversion operation')
        except:
            logger.logger.error('There was an error while doing the radians conversion operation')

    def pi(self):
        try:
           self.ent.delete('1.0',END)
           result = float(math.pi)
           self.ent.insert(INSERT,result)
           logger.logger.info('Tried doing the pi operation')
        except:
            logger.logger.error('There was an error while doing the pi operation')

    def sqr(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(x**2)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the square operation')
        except:
            logger.logger.error('There was an error while doing the squuare operation')

    def sqrt(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = math.sqrt(x)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the square root operation')
        except Exception as e:
            logger.logger.error(e)

    def cube(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(x**3)
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the cube operation')
        except:
            logger.logger.error('There was an error while doing the exponential operation')

    def cube_rt(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(x**(1/3))
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the exponential operation')
        except Exception as e:
            logger.logger.error(e)

    def factorial(self):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(math.factorial(int(x)))
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the factorial operation')
        except Exception as e:
            logger.logger.error(e)

    def perm(self,event):
        try:
            x = float(self.ent.get('1.0',END))
            self.ent.delete('1.0',END)
            result = float(math.perm(int(x)))
            self.ent.insert(INSERT,result)
            logger.logger.info('Tried doing the perm operation')
        except Exception as e:
            logger.logger.error(e)

class operations():
    def __init__(self, ent):
        self.ent = ent


        self.state = ''
        self.x = ''
        self.y = ''
    
    def addition(self):
        self.state = 'add'
        self.x = float(self.ent.get('1.0',END))
        self.ent.insert(INSERT,'+')
        self.ent.delete('1.0',END)

    def subtract(self):
        self.state = 'subt'
        self.x = float(self.ent.get('1.0',END))
        self.ent.insert(INSERT,'-')
        self.ent.delete('1.0',END)

    def multiply(self):
        self.state = 'multi'
        self.x = float(self.ent.get('1.0',END))
        self.ent.insert(INSERT,'x')
        self.ent.delete('1.0',END)

    def division(self):
        self.state = 'divide'
        self.x = float(self.ent.get('1.0',END))
        self.ent.insert(INSERT,'/')
        self.ent.delete('1.0',END)

    def equals(self):

        if self.state == 'add':
            try:
                self.y = float(self.ent.get('1.0',END))
                self.result = self.x + self.y
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT, float(self.result))
            except Exception as e:
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT,'Math Error!')
                logger.logger.error(e)
        elif self.state == 'subt':
            try:
                self.y = float(self.ent.get('1.0',END))
                self.result = self.x - self.y
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT, float(self.result))
            except Exception as e:
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT,'Math Error!')
                logger.logger.error(e)        
        elif self.state == 'multi':
            try:
                self.y = float(self.ent.get('1.0',END))
                self.result = self.x * self.y
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT, float(self.result))
            except Exception as e:
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT,'Math Error!')
                logger.logger.error(e)
        elif self.state == 'divide':
            try:
                self.y = float(self.ent.get('1.0',END))
                self.result = self.x / self.y
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT, float(self.result))
            except Exception as e:
                self.ent.delete('1.0',END)
                self.ent.insert(INSERT,'Math Error!')
                logger.logger.error(e)
                
  

if __name__ == '__main__':
    Maths(ent=Tk())