# 记录SQLServer的一些点

* 分页查找

```sql
    select [column1]
        ,[column2]
        ...     
        ,[columnN]
    from [tableName]
    order by [columnM]
    offset (pageIndex-1)*pageSize rows
    fetch next pageSize rows only
```

> 在*Sql Server 2012*之前，实现分页主要是使用ROW_NUMBER()，在SQL Server2012，可以使用Offset ...Rows  Fetch Next ... Rows only的方式去实现分页数据查询。</br>
> **使用Offset /Fetch Next需要指定排序，即必须有order by(数据库版本必须大于2008)**
