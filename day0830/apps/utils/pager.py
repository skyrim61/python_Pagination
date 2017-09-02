#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'xurui'
__date__ = '2017/9/2 9:04'


class PageInfo(object):
    def __init__(self, current_page, all_count, base_url, per_page=20, show_page=11):  ## show_page,最多显示11个页码
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        self.base_url = base_url
        # a, b = divmod(self.all_count, self.per_page)
        a, b = divmod(all_count, per_page)
        if b:
            a = a + 1
        self.all_page = a
        self.show_page = show_page

    def start(self):
        return (self.current_page - 1) * self.per_page

    def end(self):
        return self.current_page * self.per_page

    def pager(self):
        # v = "<a href='/app01/index.html/?page=1'>1<a>"
        # return v
        page_list = []
        half = int((self.show_page - 1) / 2)  ##5
        # begin = self.current_page - half  ##11-5=6
        # stop = self.current_page + half + 1  ##11+5+1

        ##如果数据总页数 < 11
        if self.all_page < self.show_page:  ## 页数小于 11,有几页显示几页,但是,页数>=11的话,会出现负数
            begin = 1
            stop = self.all_page + 1
        ##如果数据总页数 > 11
        else:
            ###前提:all_page>=11页,如果当前页<=5, 永远显示1到11页
            if self.current_page <= half:
                begin = 1
                stop = self.show_page + 1
            else:
                ##前提:当前页>5,那么就要动态的显示页数,当前页+half超过了总页数,起始页为后面11个的开头,始终保持11个
                if self.current_page + half > self.all_page:
                    begin = self.all_page - self.show_page + 1
                    stop = self.all_page + 1
                else:
                    ##前提是不是前11个,也不是后面11页,是中间的
                    begin = self.current_page - half
                    stop = self.current_page + half + 1

        ##首页
        first_page = "<li><a href='%s?page=1'>首页</a></li>" % (self.base_url)
        page_list.append(first_page)
        ##上一页
        if self.current_page <= 1:
            prev_page = "<li><a href='%s?page=1'>上一页</a></li>" % (self.base_url)
        else:
            prev_page = "<li><a href='%s?page=%s'>上一页</a></li>" % (self.base_url, self.current_page - 1)
        page_list.append(prev_page)
        ##所有页
        # for i in range(1,self.all_page+1):
        for i in range(begin, stop):
            if i == self.current_page:
                temp = "<li class='active'><a href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>" % (self.base_url, i, i,)
            page_list.append(temp)
        ##下一页
        if self.current_page >= self.all_page:
            next_page = "<li><a href='%s?page=%s'>下一页</a></li>" % (self.base_url, self.all_page)
        else:
            next_page = "<li><a href='%s?page=%s'>下一页</a></li>" % (self.base_url, self.current_page + 1)
        page_list.append(next_page)
        ##尾页
        last_page = "<li><a href='%s?page=%s'>尾页</a></li>" % (self.base_url, self.all_page)
        page_list.append(last_page)

        return ''.join(page_list)
