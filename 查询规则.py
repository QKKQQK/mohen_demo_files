{
	"_id" : [match, range],
	"pid" : [match, range],
    "name" : [match],
	"flag" : [match, range],
	"exttype" : [match, range],
	"type" : [match, range],
	"tag" : [match],
	"klist" : [match],
	"rlist" : [match],
	"extlist" : {key: [match]},
	"ugroup" : [match, range],
	"uid" : [match],
	"fid" : [match],
	"eid" : [match],
	"openid" : [match],
	"v1" : [match, range],
	"v2" : [match, range],
	"v3" : {key: [match, range]}
	"cfg" : [],
	"utc_date" : [match, range],
	"utc_ts" : [match, range]
}


[filter]
who:	rlist, （extlist）, ugroup, uid, openid
where:  fid, eid, (extlist)
what:   name, exttype, type, tag, klist, (extlist)
when:   (_id), (extlist), utc_date(y/m/d/h/m/s)
how much: v1, v2, v3, (normalized)(v1, v2, v3), cfg

[Stats]
aggregate: sum, avg, min, max

[Sort]
Date, (_id？), (fid), (eid), (uid)

[Single Set Data Presentation]
x axis: $group by date [y/m/d/h/m], fid, eid...
y axis: v1, v2, v3, (normalized)(v1, v2, v3) 

[Two Set Data Presentation]
x axis [filter 1] : (normalized)(v1, v2, v3) 
y axis [filter 2] : (normalized)(v1, v2, v3) 

[Multiple Set Data Presentation]
x axis [filter 1] : alpha * (normalized)(v1, v2, v3) + \
					beta * (normalized)(v1, v2, v3) + \
					gamma * (normalized)(v1, v2, v3) 
y axis [filter 2] : (normalized)(v1, v2, v3) 

[Excel Tree Structure]