
# Overwatcher: Overwatch League Statistics API

`overwatcher` provides API for accessing [Overwatch
League](https://overwatchleague.com/) statics on match, map and player
level.

The data comes from two sources:

-   [Overwatch League Stats
    Lab](https://overwatchleague.com/zh-cn/statslab) including match and
    map statistics for all 4 seasons, currently only season 4 match
    statistics is presented in the app

-   [Liquipedia Player Wiki](https://liquipedia.net/overwatch/Players)
    including players’ personal information

## Tehcnologies

All API endpoints and swagger docs are implemented in Python’s
[FastAPI](https://fastapi.tiangolo.com/) framework. Data cleaning and
scraping is done in R with
[data.table](https://rdatatable.gitlab.io/data.table/).

## Available Query Parameters and values

When it comes to match statistics, there are 3 important query
parameters to pre-filter data and limit the analysis scope: stat, hero
and map. For example, we may be interested to know how fleta’s
performance on tracer in Ilios, specifically, the average played time,
hero damage and time alive. Then we can set query parameters on swagger
as

<img src="screenshots/set-query-parameters.png" />

This generates curl commands

``` bash
curl -X 'GET' \
  'http://127.0.0.1:8000/player_stat/fleta?stat=all%20damage%20done&stat=time%20alive&stat=time%20played&hero=tracer&map=ilios' \
  -H 'accept: application/json'
```

Below is a list of all available values for heroes, maps and stats. Note
that all values should be lowercase.

### heroes

(ordered alphabetically)

-   `all heroes`
-   `ana`
-   `ashe`
-   `baptiste`
-   `bastion`
-   `brigitte`
-   `d.va`
-   `doomfist`
-   `echo`
-   `genji`
-   `hanzo`
-   `junkrat`
-   `lucio`
-   `mccree`
-   `mei`
-   `mercy`
-   `moira`
-   `orisa`
-   `pharah`
-   `reaper`
-   `reinhardt`
-   `roadhog`
-   `sigma`
-   `soldier: 76`
-   `sombra`
-   `symmetra`
-   `torbjorn`
-   `tracer`
-   `widowmaker`
-   `winston`
-   `wrecking ball`
-   `zarya`
-   `zenyatta`

# maps

(ordered alphabetically)

-   `blizzard world`
-   `busan`
-   `dorado`
-   `eichenwalde`
-   `hanamura`
-   `havana`
-   `hollywood`
-   `ilios`
-   `junkertown`
-   `king's row`
-   `lijiang tower`
-   `nepal`
-   `numbani`
-   `oasis`
-   `rialto`
-   `route 66`
-   `temple of anubis`
-   `volskaya industries`
-   `watchpoint: gibraltar`

## stats

(ordered by occurrences)

-   `time alive`
-   `time building ultimate`
-   `time played`
-   `time elapsed per ultimate earned`
-   `ultimates earned - fractional`
-   `average time alive`
-   `damage taken`
-   `all damage done`
-   `hero damage done`
-   `barrier damage done`
-   `deaths`
-   `eliminations`
-   `final blows`
-   `objective time`
-   `assists`
-   `healing received`
-   `time holding ultimate`
-   `objective kills`
-   `ultimates used`
-   `quick melee ticks`
-   `damage - quick melee`
-   `shots fired`
-   `weapon accuracy`
-   `quick melee accuracy`
-   `quick melee hits`
-   `shots missed`
-   `solo kills`
-   `shots hit`
-   `time hacked`
-   `time discorded`
-   `multikills`
-   `melee final blows`
-   `turrets destroyed`
-   `critical hit kills`
-   `critical hit accuracy`
-   `critical hits`
-   `damage - weapon`
-   `environmental deaths`
-   `offensive assists`
-   `self healing`
-   `self healing percent of damage taken`
-   `knockback kills`
-   `defensive assists`
-   `damage blocked`
-   `damage - weapon primary`
-   `healing done`
-   `environmental kills`
-   `damage - weapon secondary`
-   `players knocked back`
-   `scoped shots`
-   `damage amplified`
-   `damage - weapon scoped`
-   `scoped accuracy`
-   `scoped hits`
-   `recon assists`
-   `healing - weapon`
-   `healing amplified`
-   `primary fire ticks`
-   `secondary fire accuracy`
-   `primary fire accuracy`
-   `primary fire hits`
-   `scoped critical hit accuracy`
-   `scoped critical hits`
-   `infra-sight efficiency`
-   `scoped critical hit kills`
-   `ultimates negated`
-   `damage done`
-   `damage - sticky bombs`
-   `sticky bombs direct hit accuracy`
-   `sticky bombs direct hits`
-   `sticky bombs useds`
-   `damage - emp`
-   `emp efficiency`
-   `enemies emp'd`
-   `enemies hacked`
-   `average players per teleporter`
-   `players teleported`
-   `teleporter uptime`
-   `teleporters placed`
-   `melee percentage of final blows`
-   `damage - fire strike`
-   `rocket hammer melee accuracy`
-   `rocket hammer melee average targets`
-   `rocket hammer melee hits`
-   `rocket hammer melee hits - multiple`
-   `rocket hammer melee ticks`
-   `damage - jump pack`
-   `damage - primal rage leap`
-   `damage - primal rage melee`
-   `damage - primal rage total`
-   `jump pack kills`
-   `melee kills`
-   `primal rage efficiency`
-   `primal rage kills`
-   `primal rage melee accuracy`
-   `primal rage melee efficiency`
-   `primal rage melee hits`
-   `primal rage melee hits - multiple`
-   `primal rage melee ticks`
-   `tesla cannon accuracy`
-   `tesla cannon efficiency`
-   `tesla cannon hits`
-   `tesla cannon hits - multiple`
-   `tesla cannon ticks`
-   `weapon kills`
-   `grappling claw uses`
-   `roll uptime`
-   `roll uptime percentage`
-   `roll uses`
-   `biotic grenade kills`
-   `damage - biotic grenade`
-   `healing - biotic grenade`
-   `healing - weapon scoped`
-   `nano boost assists`
-   `nano boost efficiency`
-   `nano boosts applied`
-   `sleep dart shots`
-   `unscoped accuracy`
-   `unscoped hits`
-   `unscoped shots`
-   `amplification matrix casts`
-   `biotic launcher healing explosions`
-   `biotic launcher healing shots`
-   `damage prevented`
-   `healing - biotic launcher`
-   `healing - regenerative burst`
-   `healing accuracy`
-   `biotic orb damage efficiency`
-   `biotic orb healing efficiency`
-   `biotic orb maximum damage`
-   `biotic orb maximum healing`
-   `coalescence healing`
-   `coalescence kills`
-   `coalesence - damage per use`
-   `coalesence - healing per use`
-   `damage - biotic orb`
-   `damage - coalescence`
-   `healing - biotic orb`
-   `healing - coalescence`
-   `healing - secondary fire`
-   `secondary fire hits`
-   `secondary fire ticks`
-   `damage - boosters`
-   `damage - micro missiles`
-   `damage - pistol`
-   `mech deaths`
-   `mechs called`
-   `self-destructs`
-   `armor - rally`
-   `armor provided`
-   `damage - shield bash`
-   `healing - inspire`
-   `healing - repair pack`
-   `inspire uptime`
-   `inspire uptime percentage`
-   `rally armor efficiency`
-   `amped heal activations`
-   `amped speed activations`
-   `heal song time elapsed`
-   `healing - healing boost`
-   `healing - healing boost amped`
-   `sound barrier casts`
-   `sound barrier efficiency`
-   `sound barriers provided`
-   `soundwave kills`
-   `speed song time elapsed`
-   `ability damage done`
-   `damage - rising uppercut`
-   `damage - rocket punch`
-   `damage - seismic slam`
-   `shields created`
-   `damage - pulse bomb`
-   `health recovered`
-   `match blinks used`
-   `pulse bomb attach rate`
-   `pulse bomb efficiency`
-   `pulse bomb kills`
-   `pulse bombs attached`
-   `recalls used`
-   `enemies slept`
-   `sleep dart hits`
-   `sleep dart success rate`
-   `healing - immortality field`
-   `damage - discord orb`
-   `damage - weapon charged`
-   `discord orb time`
-   `harmony orb time`
-   `healing - harmony orb`
-   `healing - transcendence`
-   `transcendence efficiency`
-   `transcendence healing`
-   `transcendence percent of healing`
-   `damage - duplicate`
-   `damage - focusing beam`
-   `damage - focusing beam - bonus damage only`
-   `duplicate kills`
-   `focusing beam accuracy`
-   `focusing beam dealing damage seconds`
-   `focusing beam kills`
-   `focusing beam seconds`
-   `sticky bombs kills`
-   `damage - coach gun`
-   `damage - dynamite`
-   `damage - deadeye`
-   `damage - flashbang`
-   `deadeye efficiency`
-   `deadeye kills`
-   `fan the hammer kills`
-   `adaptive shield uses`
-   `air uptime`
-   `air uptime percentage`
-   `damage - grappling claw`
-   `damage - minefield`
-   `damage - piledriver`
-   `damage taken - adaptive shield`
-   `damage taken - ball`
-   `damage taken - tank`
-   `grappling claw impacts`
-   `grappling claw kills`
-   `minefield kills`
-   `piledriver kills`
-   `piledriver uses`
-   `shielding - adaptive shield`
-   `damage - self destruct`
-   `accretion kills`
-   `accretion stuns`
-   `damage - accretion`
-   `damage - hyperspheres`
-   `damage absorbed`
-   `gravitic flux damage done`
-   `gravitic flux kills`
-   `hyperspheres direct hits`
-   `damage - dragonstrike`
-   `damage - storm arrows`
-   `storm arrow kills`
-   `average energy`
-   `damage - graviton surge`
-   `energy maximum`
-   `graviton surge efficiency`
-   `graviton surge kills`
-   `high energy kills`
-   `lifetime energy accumulation`
-   `projected barrier damage blocked`
-   `projected barriers applied`
-   `amplification matrix assists`
-   `amplification matrix efficiency`
-   `immortality field deaths prevented`
-   `self destruct efficiency`
-   `self-destruct kills`
-   `players halted`
-   `supercharger assists`
-   `supercharger efficiency`
-   `damage - deflect`
-   `damage - dragonblade`
-   `damage - dragonblade total`
-   `damage - swift strike`
-   `damage - swift strike dragonblade`
-   `damage reflected`
-   `dragonblade efficiency`
-   `dragonblade kills`
-   `dragonblades`
-   `damage - call mech`
-   `healing - weapon valkyrie`
-   `players resurrected`
-   `players saved`
-   `valkyrie healing efficiency`
-   `blaster kills`
-   `damage - weapon pistol`
-   `damage - blizzard`
-   `freeze spray damage`
-   `icicle damage`
-   `damage - charge`
-   `bob gun damage`
-   `bob kills`
-   `damage - bob`
-   `damage - bob charge`
-   `dynamite kills`
-   `damage - sonic`
-   `dragonstrike efficiency`
-   `dragonstrike kills`
-   `biotic field healing done`
-   `biotic fields deployed`
-   `damage - helix rockets`
-   `helix rocket kills`
-   `damage - barrage`
-   `direct hit accuracy`
-   `rocket barrages`
-   `rocket direct hits`
-   `of rockets fired`
-   `secondary direct hits`
-   `torbj`
-   `turret damage`
-   `coach gun kills`
-   `teleporter pads destroyed`
-   `blizzard efficiency`
-   `blizzard kills`
-   `enemies frozen`
-   `successful freezes`
-   `total time frozen`
-   `damage - earthshatter`
-   `earthshatter stuns`
-   `fire strike kills`
-   `charge kills`
-   `earthshatter efficiency`
-   `earthshatter kills`
-   `damage - tactical visor`
-   `tactical visors`
-   `barrage efficiency`
-   `barrage kills`
-   `damage - sentry turret`
-   `photon projector kills`
-   `primary fire average level`
-   `primary fire hits hits - level`
-   `damage - molten core`
-   `turret kills`
-   `overload kills`
-   `damage - death blossom`
-   `death blossoms`
-   `tactical visor efficiency`
-   `tactical visor kills`
-   `hooks attempted`
-   `sentry turret kills`
-   `molten core efficiency`
-   `molten core kills`
-   `damage - venom mine`
-   `death blossom efficiency`
-   `death blossom kills`
-   `damage - meteor strike`
-   `deflection kills`
-   `infra-sight uptime`
-   `meteor strike efficiency`
-   `meteor strike kills`
-   `venom mine kills`
-   `damage - chain hook`
-   `enemies hooked`
-   `hook accuracy`
-   `damage - whole hog`
-   `whole hog efficiency`
-   `whole hog kills`
-   `damage - concussion mine`
-   `frag launcher direct hits`
-   `damage - weapon sentry`
-   `concussion mine kills`
-   `damage - weapon hammer`
-   `hammer kills`
-   `damage - weapon recon`
-   `sentry kills`
-   `damage - steel trap`
-   `enemies trapped`
-   `recon kills`
-   `damage - rip-tire`
-   `rip-tire efficiency`
-   `rip-tire kills`
-   `damage - weapon tank`
-   `damage - total mayhem`
-   `tank efficiency`
-   `tank kills`
-   `total mayhem kills`
