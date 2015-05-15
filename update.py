import gspread

def main():
	data = get_data('lvtr4n@gmail.com', 'dummyaccount', 'projectapollo')
	input  = ""
	for d in data:
		input += '\t\t\t<tr>\n\t\t\t\t<td class="title">%s</td>\n\t\t\t\t<td>%s</td></tr>\n' % (d[0], d[1])
	update("index.html", input, 66)

def get_data(usr, pwd, source):
	gc = gspread.login(usr, pwd)
	wks = gc.open(source).sheet1
	cell_list = wks.get_all_values()
	result = []
	for pair in cell_list:
		result.append((pair[0], pair[1]))
	return result

def update(file_name, input, start_line):
	data = open(file_name, "r").readlines()			#Open file to read all data
	data[start_line] = data[start_line] + input		#Add new data into specified line
	open(file_name, 'w').close()				#Flush entire file
	open(file_name, 'w').writelines(data)			#Rewrite with new data
main()
