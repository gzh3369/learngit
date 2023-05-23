# 功能：文档操作模块，包含以下6个函数：
'''
copy_files(source_folder_name, target_folder, file_extension = 'xlsx')        批量复制指定后缀名文件
delete_files(source_folder_name, file_extension = 'xlsx')                     批量删除指定后缀名文件
move_files(source_folder_name, target_folder, file_extension = 'xlsx')        批量移动指定后缀名文件
walk_to_find(find_path, find_file_name)                                       在路径find_path中递归寻找文件find_file_name
find_extension(find_path, extension_name = "xlsx,mp3")                        递归查找指定后缀名的文件
stat_file(folder_name)                                                        统计指定目录下文件和文件夹个数
'''
# 作者：gezhihao
# 时间：20230523

import os,shutil

def copy_files(source_folder_name, target_folder, file_extension = 'xlsx'):
    """
    批量复制指定后缀名文件
    :param source_folder_name:
    :param target_folder:
    :param file_extension:
    :return:
    """
    cp_files = []
    for root, folders, files in os.walk(source_folder_name):
        for cur_file in files:
            if os.path.splitext(cur_file)[1] == '.'+file_extension:
                cp_files.append(os.path.join(root,cur_file))
    
    # 复制这些文件
    for cp_file in cp_files:
        shutil.copy(cp_file,target_folder)
    print('Done')

# copy_files(r"C:\Users\Demo\Documents\GithubStudy", r'C:\Users\Demo\Documents\GithubStudy\pythonlearn','py')

def delete_files(source_folder_name, file_extension = 'xlsx'):
    """
    批量删除指定后缀名文件
    :param source_folder_name:
    :param file_extension:
    :return:
    """
    del_files = []
    for root, folders, files in os.walk(source_folder_name):
        for cur_file in files:
            if os.path.splitext(cur_file)[1] == '.'+file_extension:
                del_files.append(os.path.join(root,cur_file))
    
    # 删除这些文件
    for del_file in del_files:
        os.remove(del_file)
    print('Done')
    
# delete_files(r'C:\Users\Demo\Documents\GithubStudy\pythonlearn','py')

def move_files(source_folder_name, target_folder, file_extension = 'xlsx'):
    """
    批量移动指定后缀名文件
    :param source_folder_name:
    :param target_folder:
    :param file_extension:
    :return:
    """
    mv_files = []
    for root, folders, files in os.walk(source_folder_name):
        for cur_file in files:
            if os.path.splitext(cur_file)[1] == '.'+file_extension:
                mv_files.append(os.path.join(root,cur_file))
    
    # 剪切这些文件
    for mv_file in mv_files:
        if os.path.exists(os.path.join(target_folder,os.path.basename(mv_file))):
            continue
        shutil.move(mv_file,target_folder)
    print('Done')

# move_files(r"C:\Users\Demo\Documents\GithubStudy\pythonlearn",r'C:\Users\Demo\Documents\GithubStudy\pythonlearn\test','py')

def walk_to_find(find_path, find_file_name):
    """
    在路径find_path中递归寻找文件find_file_name
    :param find_path:
    :param find_file_name:
    :return:
    """
    result_path = []
    for root, dirs, files in os.walk(find_path):
        for item in files:
            if item == find_file_name:
                file_path = os.path.join(root, item)
                result_path.append(file_path)
    
    if len(result_path) > 0:
        print("找到文件")
        print("\n".join(result_path))
    else:
        print("文件未找到")
    return result_path

# walk_to_find(r'C:\Users\Demo\Documents\GithubStudy','0模块.py')

def find_extension(find_path, extension_name = "xlsx,mp3"):
    """
    递归查找指定后缀名的文件
    :param find_path:
    :param extension_name:
    :return:
    """
    tmp_extensions = extension_name.split(",")
    extensions = ['.' + item for item in tmp_extensions]

    result_path = []
    for cur_dir, folders, files in os.walk(find_path):
        for item in files:
            extension = os.path.splitext(item)[1].lower()
            if extension in extensions:
                result_path.append(os.path.join(cur_dir, item))
        
    if len(result_path) > 0:
        print("\n".join(result_path))
    else:
        print("文件未找到")

# find_extension(r'C:\Users\Demo\Documents\GithubStudy','py,txt')

def stat_file(folder_name):
    '''
    统计文件个数，文件夹个数
    :para folder_name:
    :return:
    '''
    file_count, folder_count = 0, 0
    if folder_name:
        for dir, folders, files in os.walk(folder_name):
            file_count += len(files)
            folder_count += len(folders)
        print(f"{folder_name}里一共包含：{file_count}个文件，{folder_count}个文件夹")
    return file_count,folder_count

# stat_file(r'C:\Users\Demo\Documents\GithubStudy')