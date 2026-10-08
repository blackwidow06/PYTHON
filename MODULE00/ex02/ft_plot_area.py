# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: malavaud <malavaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/08 11:02:57 by malavaud          #+#    #+#              #
#    Updated: 2026/10/08 15:00:17 by malavaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	lenght = int(input("Enter lenght: "))
	width = int(input("Enter width: "))
	area = lenght * width
	print("Plot area:", area)