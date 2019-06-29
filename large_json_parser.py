import sys

def parse_json(file):

	def _parse_attribute(attr):
		if attr.endswith(','):
			value = attr[attr.index(':')+3:len(attr)-2]
		else:
			value = attr[attr.index(':')+3:len(attr)-1]

		return value

	try:
		with open(file) as f:
			row = ''
			for line in f:
				l = line.strip()

				if l in ['[', ']', '{']:
					row = ''
				elif l in ['}', '},']:
					print(row)
				else:
					row += _parse_attribute(l) + ','
	except IOError:
		print('Error: File %s can not be found' % file)


def main():
	try:
		filename = sys.argv[1]
	except IndexError:
		print('Error: File location must be specified')

	parse_json(filename)


if __name__ == '__main__':
	main()