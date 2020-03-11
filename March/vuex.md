store.js

```json
state: // data
getters: // computed
{allUsersCount: function(state) {
    return state.allUsers.length
  },
  countSeoul: state => {
    let count = 0
    state.allUsers.forEach(user => {
      if(user.address == 'Seoul') count ++
    })
    return count
  },
   percentOfSeoul: (state, getters) => {
     return Math.round(getters.percenofSeoul / getters.allUserCount * 100)
   }
}
mutations:
actions:
```



원래 파일

```vue
<script>
 <h2>{{$store.getters.allUsersCount}}</h2>
 <h2>{{ percentOfSould }}</h2>
 <-- mapgetters 이용하기 -->
 <v-for="(user, index)" in $store.state.allUsers"   
</script>
<template>
import { mapGetters } from 'vuex' 
data() {
  return {
		
  }
},
computed: {
  ...mapGetters(['allUsersCount', 'countOfSould, 'percentSeoul]) // 불러오기
}
</template>
```

main.js

