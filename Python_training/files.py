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
if 1:
    #https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/#:~:text=In%20Python%2C%20arguments%20are%20passed,used%20to%20parse%20named%20arguments.
    import sys
    import getopt

    def myfunc(argv):
        folder_name = ""
        project_name = ""
        project_path = ""
        arg_help = "{0} -f <repo_folder_name> -p <project_name> -pp <path_where_to_execute>".format(argv[0])
        
        try:
            opts, args = getopt.getopt(argv[1:], "h:f:pp:p:", ["help", "foldername=", 
            "project_path=", "project_name="])
        except:
            print(arg_help)
            sys.exit(2)
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(arg_help)  # print the help message
                sys.exit(2)
            elif opt in ("-f", "--foldername"):
                folder_name = arg
            elif opt in ("-pp", "--projectpath"):
                project_path = arg
            elif opt in ("-p", "--projectname"):
                project_name = arg
        
        print("opts,args",opts)

        print('repo folder name:', folder_name)
        print('project path:', project_path)
        print('project name:', project_name)
    myfunc(sys.argv)