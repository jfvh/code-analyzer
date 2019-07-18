import os
# import esprima
# import pprint

directory = '/Users/jvanheijst/projects/frontend/conversational-ui';
print('analyzing project ' + directory)
filecount = 0;
linecount = 0;
maxlines =0;
biggestFile ='';

# declaring histogram
result_label =['0-25','25-50', '50-100', '100-250','250-500','500-1000','1000+']

result_value =[0,0,0,0,0,0,0];





for subdir, dirs, files in os.walk(directory):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if (filepath.endswith(".ts") or filepath.endswith(".tsx")) and not filepath.__contains__('node_modules') and not filepath.__contains__('__tests__') :
            count = len(open(filepath).readlines())
            filecount += 1;
            linecount += count;
            if(count >0 and count <=25):
                result_value[0] = result_value[0] + 1;
            if (count > 25 and count <= 50):
                result_value[1] = result_value[1] + 1;
            if (count > 50 and count <= 100):
                result_value[2] = result_value[2] + 1;
            if (count > 100 and count <= 250):
                result_value[3] = result_value[3] + 1;
            if (count > 250 and count <= 500):
                result_value[4] = result_value[4] + 1;
            if (count > 500 and count <= 1000):
                result_value[5] = result_value[5] + 1;
            if  (count >1000):
                result_value[6] = result_value[6] + 1;



            if(count > maxlines) :
                maxlines=count;
                biggestFile = filepath;


            # print (filepath + ' - '+ str(count))
avlines = linecount / filecount;
print ('average lines per file - ' + str(avlines))
print ('biggest file           - ' + str(maxlines) + ' ('+biggestFile+')')

print(' ');
print('file sizes:')
for i in range(0, 7):
    print (result_label[i] + ' - ' + str(result_value[i]))


#
# # pprint(esprima.parseScript('/Users/jvanheijst/projects/frontend/conversational-ui'));
# str = open('/Users/jvanheijst/projects/frontend/conversational-ui/src/services/MessagesService/MessagesService.ts', 'r').read()
# print(esprima.parseScript(str))
