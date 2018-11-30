## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:mood_affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:mood_deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremly sad
- so sad

## intent:inbox
- show me my inbox items
- show me [high](priority) priority items in my inbox
- what is there in my inbox
- whats up
- what should i do today

## intent:dashboard
- plot dashboard for my projects
- plot organization dashboard
- show me my dashboard
- what is the status of the project

## intent:group-by-priority
- Group by Priority

## intent:release_num
- [4.0.0](release_no) [5](build_no)
- release [4.6.0](release_no) build [8](build_no)

## intent:group-by-item-type
- Group by Item-type

## lookup:priority
- High
- Critical
- low

## intent:release
- show me release [4.6.9](release_no) build [4](build_no) info
- what is the status of release [5.0.0](release_no) and build [9](build_no)
- get me release [4.5.6](release_no) build [10](build_no) status
- show me release [4.5.6](release_no) and build [33] data

## intent:change
- how many files has been changed
- total files affected

## intent:files_modified
- show me files modified
- list me files changed

## intent:build
- what is the build status
- show me build information

## intent:jenkins jobs
- fire job
- run jenkins job

## intent:performance
- perf report
- show performance report

## intent:sahifailedsummary
- failed sahi result
- show me automation result

## intent:register
- register jenkins job

## intent:junitresult
- show junit result
- get junit reports

## intent:sonar
- show me code quality
- code quality report

## intent:connectionleak
- is there any connnection leak
- show me the connection leaks
## regex:release_no
- (\d+)\.(\d+)\.(\d+)

## regex:build_no
- (\d+)
