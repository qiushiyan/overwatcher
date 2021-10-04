## Available Query Parameters and values

When it comes to match statistics, there are 3 important query paramters to pre-filter data and limit the analysis scope: stat, hero and map. For exmaple, we may be interested to know how fleta's performane on tracer in Ilios, specifically, the average played time, hero damage and time alive. Then we can set query paramters as

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/player_stat/fleta?stat=all%20damage%20done&stat=time%20alive&stat=time%20played&hero=tracer&map=ilios' \
  -H 'accept: application/json'
```

![](/screenshots/set-query-parameters.jpg)

### hero
