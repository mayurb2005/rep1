total_land = 80 
each_plot = 80/5
tomato_output = (( 0.3 * each_plot ) * 10 * 1000) + ( ( 0.3 * each_plot ) * 12 * 1000)
tomato_sales = 7 * tomato_output

potato_output = 10 * each_plot * 1000
potato_sales = potato_output * 20

cabbage_output = 14 * each_plot * 1000
cabbage_sales = cabbage_output * 24

sunflowers_output = 0.7 * each_plot * 1000
sunflowers_sales = sunflowers_output * 200

sugarcane_output =  45 * each_plot 
sugarcane_sales = sugarcane_output * 4000


total_sales = tomato_sales + potato_sales + cabbage_sales + sugarcane_sales + sunflowers_output
print("Total Sales :", total_sales)

chemical_free_sales = total_sales-sunflowers_sales
