import pdfkit


# pdfkit.from_string(html,'out3.pdf')
pdfkit.from_url('http://timetable.ugrasu.ru/index.php/timetable/show_timetable/group/4575', 'out.pdf')