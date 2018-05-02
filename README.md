# STDS

STDS는 **S**elf **T**est **D**riven **S**tudy의 약어로, TDD에서 착안했습니다.
<br>
혼자 공부를 하는데 주관적으로 학습을 많이 했다고 생각하는 것이 아닌, 
<br>
목표치를 두고 정말 확실히 공부를 잘 했는지 알아보기 위한 자기검증수단입니다.

## Usage

> 1. stds-problems.txt에 '\n'을 개행구분자로 문제를 입력합니다.
> 2. `python stds-supervisor.py`를 실행하면 10개의 랜덤 선택된 문제가 출력됩니다. 
> 3. shell command로 매일의 출제 문제를 저장할 수 있습니다.

참고사항: 출제할 문제의 수나 파일명 변경은 stds-supervisor.py에서 수정해주시면 됩니다.
## Example
```shell
python stds-supervisor.py > daily_test.txt 
```

