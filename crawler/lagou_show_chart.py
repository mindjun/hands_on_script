from pyecharts import Geo

city_datas = [('北京', 149), ('上海', 95), ('深圳', 77), ('成都', 22), ('杭州', 17), ('广州', 17), ('武汉', 16),
              ('南京', 13), ('苏州', 7),
              ('郑州', 5), ('天津', 4), ('西安', 4), ('东莞', 3), ('珠海', 2), ('合肥', 2), ('厦门', 2),
              ('宁波', 1), ('南宁', 1), ('重庆', 1),
              ('佛山', 1), ('大连', 1), ('哈尔滨', 1), ('长沙', 1), ('福州', 1), ('中山', 1)]
geo = Geo("Python岗位城市分布地图", "数据来源拉勾", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(city_datas)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff",
        symbol_size=15, is_visualmap=True)
geo.render("Python岗位城市分布地图_scatter.html")

geo = Geo("Python岗位城市分布地图", "数据来源拉勾", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(city_datas)
geo.add("", attr, value, type="heatmap", visual_range=[0, 10], visual_text_color="#fff",
        symbol_size=15, is_visualmap=True)
geo.render("Python岗位城市分布地图_heatmap.html")
