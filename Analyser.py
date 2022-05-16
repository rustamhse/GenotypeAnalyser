import PySimpleGUI as sg
import textract

log = []
search_input = []
log_f = []
SNPs = []
Alleles = []

layout = [[sg.Text('Данная программа позволяет анализировать геном человека на наличие SNP и их аллелей')],
          [sg.Text('>> Выберите файл с генотипом'), sg.FileBrowse('Файл')],
          [sg.Input('Введите необходимые SNP через пробел', size=(90), key = 'snps')],
          [sg.Button('Анализировать'), sg.Button('Ввести SNP, характерные для ВИЧ', key = 'HIV')],
          [sg.Output(size=(88, 20), key = 'output')]
          ]
window = sg.Window('Анализатор генотипа', layout)

while True:
    event, values = window.read()    
    if event == sg.WIN_CLOSED:
        break    
    
    if event == 'HIV':
         window['snps'].update('rs333 rs9264942 rs2395029 rs2572886 rs4418214 rs3131018')
    
    if event == 'Анализировать':
        
        log.clear()
        search_input.clear()
        log_f.clear()
        SNPs.clear()
        Alleles.clear()
        
        window['output'].Update('')
        
        if values['Файл'] != '':
            with open(values['Файл'], 'rt') as f:
                data = f.readlines()
                
            if values['snps'] != 'Введите необходимые SNP через пробел':
                search_input = values['snps'].split(' ')
                
                print('Выполняется анализ генотипа... \n')

                for query in search_input:
                    for line in data:
                        if query in line:
                            format_line = ' '.join(line.split())
                            log.append(format_line)

                for query in log:
                    if query.split(' ')[0] in search_input:
                        log_f.append(query)

                for queries in log_f:
                    SNPs.append(queries.split(' ')[0])
                    Alleles.append(queries.split(' ')[3])

                for query in search_input:
                    if query not in SNPs:
                        print(" <!> Полиморфизм " + query + " не найден в геноме")

                for i in range (0, len(SNPs)):
                    print(SNPs[i] + ' == ' + Alleles[i])
                
            else:
                print('Вы не ввели SNP!')
                    
        else:
            print('Вы не выбрали файл!')
    
window.close()