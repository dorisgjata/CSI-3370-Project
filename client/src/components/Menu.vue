<template>
    <b-table :data="msg" width="100%" >
        <template slot-scope="props">
                <b-table-column field="name" label="Period Name" width="50">
                    {{ props.row.name }}
                </b-table-column>
                <b-table-column field="categories"  label="Category Name" width="100" >
                    <b-field > 
                        <b-select v-model="filters" >
                            <option
                        
                                v-for="category in props.row.categories"
                                :value="category.id"
                                :key="category.id">
                                {{ category.name }}
                            </option>
                        </b-select>
                    </b-field>                    
               
           <!--      <b-table-column label="Items">
                     <b-select v-model="items">
                       <option
                        :key="item.itemid"
                        :value="item.itemid"
                         v-for="item  in category.items">
                         {{ item.name }}</option>
                       </b-select>    
                </b-table-column> -->
                                </b-table-column>


            </template>
    </b-table>

</template>


<script>
import axios from 'axios';
const data = require('../assets/menu.json')

export default {
  name: 'Menu',
  data() {
    return {
                        columns: [                    
                    {
                        field: 'name',
                        label: 'Period Name ',
                    },
                    {
                        field: 'periods',
                        label: 'Periods',
                    },
                    {
                        field: 'periods.categories.name',
                        label: 'Category',
                    },
                    ],
     // msg: [],
     msg: data.menu.periods,
      filters: [],
      items: []
    };
  },
 /*  methods: {
    getLocations() {
      const path = 'http://localhost:5000/menu';
      axios.get(path)
        .then((res) => {
          console.log(res);  
          this.msg = res.data.menu.periods;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getLocations();
  }, */
};
</script>