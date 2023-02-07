import os
import subprocess


def main():
    # get raw info about names of all users on a current computer.
    command = ['wmic', 'useraccount', 'get', 'name']
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, encoding='cp1252')
    output = proc.stdout.read().splitlines()

    # clean output and save users in the list without title
    user_list = [user.strip() for user in output[1:] if user]

    # run command 'net user username' for every username in user_lst
    net_cmd = ['net', 'user']  # template for command
    current_dir = os.getcwd()  # get path to working directory

    for username in user_list:  # iterate through all usernames
        net_cmd.append(username)  # create command
        user_detail_info = subprocess.Popen(net_cmd, stdout=subprocess.PIPE, shell=True,
                                            text=True)
        with open(rf'{current_dir}\user_{username}.txt', 'w') as f:
            print(user_detail_info.stdout.read(), file=f)
        user = net_cmd.pop()  # clean command template
        print(f'--->\t [v] Details for user {user} were written to file user_{user}.txt. Open it with notepad++')


if __name__ == '__main__':
    main()
