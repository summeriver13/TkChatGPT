import tkinter as tk
from gpt import openai_reply


def getTimeString():
    from time import strftime, localtime
    res = strftime("%Y-%m-%d %H:%M:%S", localtime()) + ' '
    return res


my_name = '我'
chatGPT_name = 'ChatGPT'


def getTitle(name):
    res = getTimeString() + name + '\n'
    return res


def getMessage_from_entryBox():
    # getMessage_from_entryBox
    res = entryBox.get('0.0', tk.END)
    entryBox.delete('0.0', tk.END)
    return res


def callback_sendMessage():  # 发送消息
    title = getTitle(my_name)
    messageList.insert(tk.END, title, 'greencolor')

    entry_string = getMessage_from_entryBox()
    messageList.insert(tk.END, entry_string)

    title = getTitle(chatGPT_name)
    messageList.insert(tk.END, title, 'greencolor')

    string = openai_reply(entry_string)
    messageList.insert(tk.END, string)


if __name__ == "__main__":

    root = tk.Tk()
    root.title('TkChatGPT')

    """ Top """

    # 容器
    frameTop = tk.Frame(width=500, height=320, bg='white')
    frameTop.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
    frameTop.grid_propagate(0)

    # 消息列表
    messageList = tk.Text(frameTop)
    messageList.tag_config('greencolor', foreground='#008C00')
    messageList.grid()

    """ Mid """

    # 容器
    frameMid = tk.Frame(width=500, height=150, bg='white')
    frameMid.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
    frameMid.grid_propagate(0)

    # 输入框
    entryBox = tk.Text(frameMid)
    entryBox.grid()

    """ Bottom """

    # 容器
    frameBttom = tk.Frame(width=500, height=30)
    frameBttom.grid(row=2, column=0, columnspan=2)
    frameBttom.grid_propagate(0)

    # 按钮
    button = tk.Button(frameBttom, text='发送', width=8,
                       command=callback_sendMessage)
    button.grid(row=2, column=0)

    """ 根窗口循环 """

    root.mainloop()
