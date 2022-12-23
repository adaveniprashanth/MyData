if 0:
    import os
    print(os.getcwd())
    print(os.listdir())
    old_list = os.listdir(os.chdir('../'))
    old_dict = {}
    for i in old_list:
        old_dict[i]=os.path.getatime(i)
    for i in old_dict.items():
        print(i)
    print("##############################")
    new_list = os.listdir(os.chdir('../../'))
    new_dict = {}
    for i in new_list:
        new_dict[i]=os.path.getatime(i)
    for i in new_dict.items():
        print(i[0])
if 0:#need to practice
    # command line arguments
    import argparse
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-o", "--Output", help = "Show Output")

    # Read arguments from command line
    args = parser.parse_args()

    if args.Output:
        print("Displaying Output as: % s" % args.Output)
if 0:
    #https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/#:~:text=In%20Python%2C%20arguments%20are%20passed,used%20to%20parse%20named%20arguments.
    import sys
    import getopt
    #dummy repo folder name --> ww52_prashanth_practice
    #dummy path is --> practice
    folder_name = ""
    project_name = ""
    clone_path = ""
    def myfunc(argv):
        global folder_name
        global project_name
        global clone_path
      
        #arg_help = "{0} -f <repo_folder_name> -n <project_name> -p <path_where_to_execute>".format(argv[0])
        arg_help = """{0} -f <repo_folder_name> -p <path_where_to_clone> -n <project_name>\nsample command
        python  test.py -f 'ww52_prashanth_practice' -p 'practice' -n 'lnl'""".format(argv[0])
        
        try:
            opts, args = getopt.getopt(argv[1:], "h:f:p:n:", ["help", "foldername=",
            "pathtoclone=", "projectname="])
        except:
            print(arg_help)
            sys.exit(2)
        
        for opt, arg in opts:
          if opt in ("-h", "--help"):
              print(arg_help)  # print the help message
              print("sample command")
              print("python test.py -f 'ww52_prashanth_practice' -p '/nfs/data/...' -n 'lnl'")
              sys.exit(2)
          elif opt in ("-f", "--foldername"):
              folder_name = arg
          elif opt in ("-p", "--clonepath"):
              clone_path = arg
          elif opt in ("-n", "--projectname"):
              project_name = arg
          
        #print("opts,args",opts)
    myfunc(sys.argv)
    print('repo folder name:', folder_name)
    print('project path:', clone_path)
    print('project name:', project_name)

if 1:
    pass
    value = input("enter the data")
    print("value is ",value)