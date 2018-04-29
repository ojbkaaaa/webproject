#AUTHOR:FAN
from django.utils.safestring import mark_safe
class Page:
    # 分页的封装类
    def __init__(self,current_page,data_count,per_page_count=10,page_num = 7):
        '''
        :param current_page: 当前页
        :param data_count: 数据的总数目
        :param per_page_count: 每页显示的数目
        :param page_num: 显示几页内容
        '''
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_count=per_page_count
        self.page_num = page_num

    @property
    def start(self):
        '''
        :return: 返回得到起始
        '''
        return (self.current_page-1)*self.per_page_count
    @property
    def end(self):
        '''
        :return: 返回结束
        '''
        return self.current_page*self.per_page_count

    @property
    def total_count(self):
        '''
        :return: 返回总页数
        '''
        v, y = divmod(self.data_count, self.per_page_count)
        if y:
            v += 1
        return v

    def page_str(self,base_url):
        '''
        :param base_url: 这里是用于自定义url前缀
        :return: 返回的为页面下端要显示的跳转页的html语言的字符串
        '''
        page_list = []

        if self.total_count < self.page_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.page_num + 1) / 2:
                start_index = 1
                end_index = self.page_num + 1
            else:
                start_index = self.current_page - (self.page_num - 1) / 2
                end_index = self.current_page + (self.page_num + 1) / 2
                if self.current_page + (self.page_num + 1) / 2 > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - self.page_num + 1
        if self.current_page == 1:

            prev = '<a class="page" href="#">上一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">上一页</a>' % (base_url,self.current_page - 1)
        page_list.append(prev)

        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>' % (base_url,i, i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>' % (base_url,i, i)
            page_list.append(temp)

        if self.current_page == self.total_count:
            nex = '<a class="page" href="#">下一页</a>'
        else:
            nex = '<a class="page" href="%s?p=%s">下一页</a>' % (base_url,self.current_page + 1)
        page_list.append(nex)

        go_page = """
        <input type='text' /><a onclick="jumpTo(this,'%s?p=');">跳转</a>
        <script>
            function jumpTo(ths,base){
                var val = ths.previousSibling.value;
                location.href = base + val;
            }
        </script>
        """ %(base_url)
        page_list.append(go_page)

        page_str = "".join(page_list)
        page_str = mark_safe(page_str)
        return page_str