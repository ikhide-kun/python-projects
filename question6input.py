import streamlit as st

st.title('items app')

name = st.text_input("Please enter your name")

flour_bag_cost = 2
num_flour_bag = 4
egg_carton_cost  = 3
number_egg_carton = 2

chocolate_chip_pack_cost  = 4 
num_chocolate_chip_packs = 5 
discount = 5
total_cost_flour = flour_bag_cost * num_flour_bag
total_cost_egg = egg_carton_cost * number_egg_carton
total_cost_chocolate_chip = chocolate_chip_pack_cost * num_chocolate_chip_packs
total_amount = total_cost_chocolate_chip + total_cost_egg + total_cost_flour - discount
("Hi", name, "After using your discount", "you spent a total of $", total_amount," on your baking supplies.")