import tkinter as tk

class rest:

  def __init__(self, rest_name, rest_type):
    self.rest_name = rest_name
    self.rest_type = rest_type

  def dop_rest(self):
    print(f"название кафе: {self.rest_name}")
    print(f"тип кухни: {self.rest_type}")

  def op_rest(self):
    print(f"кафе {self.rest_name} открыто")


def z1():

  class icecream(rest):

    def __init__(self, rest_name, rest_type, vkus):
      super().__init__(rest_name, rest_type)
      self.vkus = vkus

    def spicok_vkus(self):
      print("у нас есть такие вкусы мороженого:", ", ".join(self.vkus))

  new_icecream = icecream("холодок", "кафе-мороженое", ["шоколадное", "с орешками", "клубничное"])

  new_icecream.dop_rest()
  new_icecream.op_rest()
  new_icecream.spicok_vkus()
z1()

def z2():
    class icecream(rest):
        def __int__(self,rest_name,rest_type,vkus,location,ttw):
            super().__init__(rest_name,rest_type)
            self.vkus = vkus
            self.location = location
            self.ttw = ttw
        def spicok_vkus(self):
            print("у нас есть такие вкусы мороженого:", ", ".join(self.vkus))
        def dob_vkus(self,vkus):
            self.vkus.append(vkus)
        def ubr_vkus(self,vkus):
            self.vkus.remove(vkus)
        def ckek_vkus(self,vkus):
            if vkus in self.vkus:
                print("выбранный сорт доступен в меню")
            else:
                print("выбранный сорт недоступен в меню")
    class proverka:
        def __int__(self,vkus_pr):
            self.vkus_pr = vkus_pr
        def list_proverka(self):
            print("какие есть вкусы мороженого в вафельном стаканчике:", ", ".join(self.vkus_pr))
        def dob_vkus_pr(self,vkus):
            self.vkus_pr.append(vkus)
        def ubr_vkus_pr(self,vkus):
            self.vkus_pr.remove(vkus)
        def ckek_vkus_pr(self,vkus):
            if vkus in self.vkus_pr:
                print("выбранный сорт доступен в меню")
            else:
                print("выбранный сорт недоступен в меню")
    class razmer:
        def __int__(self,razmer):
            self.razmer = razmer
        def list_razmer(self):
            print("какие есть размеры мороженого в вафельном стаканчике:", ", ".join(self.vkus_pr))
        def dob_razmer(self,vkus):
            self.razmer.append(vkus)
        def ubr_razmer(self,vkus):
            self.razmer.remove(vkus)
        def ckek_razmer(self,vkus):
            if vkus in self.razmer:
                print("выбранный размер доступен в меню")
            else:
                print("выбранный сорт недоступен в меню")

    new_icecream = icecream('холодок', 'кафе-мороженое', ['шоколадное', 'с орешками', 'клубничное'],
                             'г.Москва, ул.Победы,д.7', 'с 10:00 до 22:00')
    print(f"наше местоположение: {icecream.location}")
    print(f"время работы: {icecream.ttw}")
    new_icecream.dop_rest()
    new_icecream.op_rest()
    print()
    new_icecream.spicok_vkus()
    new_icecream.dob_vkus(input("введите вкус мороженого для добавления в меню"))
    print()
    new_icecream.spicok_vkus()
    new_icecream.ubr_vkus(input("введите вкус мороженого для того чтобы убрать его из меню"))
    print()
