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
when:   (_id), (extlist), utc_date
how much: v1, v2, v3, (normalized)(v1, v2, v3), cfg
aggregate: sum, avg, min, max