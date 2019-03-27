# .Net

记录一些.Net一些东西.

* VS查看源代码
  1. 源码下载[Reference Source](https://referencesource.microsoft.com/)
  2. nuget下一个reflector插件,f12直接可以看源码
  3. 装ReSharper
  4. [官方说明](https://docs.microsoft.com/en-us/visualstudio/ide/go-to-and-peek-definition?view=vs-2017)
     > 设置项在：选项→文本编辑器→高级→启动导航到反编译源（Vs2017 15.6版本以上）

* 反编译工具 [Other Blog](https://www.cnblogs.com/ldc218/p/8945892.html)
    1. [ILSpy](https://github.com/icsharpcode/ILSpy)开源免费
    2. [dnSpy](https://github.com/0xd4d/dnSpy)开源免费

---

Jira修改baseURL：

查找属性值

```sql
select propertyvalue from propertyentry PE
join propertystring PS on PE.id=PS.id
where PE.property_key = 'jira.baseurl'
```

修改

```sql
UPDATE ps SET PS.propertyvalue='http://{domain}:8080' from propertyentry PE
join propertystring PS on PE.id=PS.id
where PE.property_key = 'jira.baseurl'
```

---

## [SqlServer知识点](./SqlServer.md)