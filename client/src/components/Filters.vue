<template>
  <div class="conatiner">
      <button type="button" value="add" class="button" @click="isCardModalActive = true" >Add</button>

    <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Filter Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(filter, index) in msg" :key="index">
              <td>{{ filter.filterId }}</td>
              <td>{{ filter.filterName }}</td>
               <td>
                <button type="button" value="edit" class="button" @click="editFilter(filter),isUpdateModalActive = true">Update</button>
                <button type="button" class="button">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>    
  
   <b-modal :active.sync="isCardModalActive" :width="640" scroll="keep">
            <div class="card">
           
                <div class="card-content">
                  <form class="w-100" ref="addFilterModal"
                            id="add-modal"
                            title="Add a new filter"
                            hide-footer>
                    <section>
                        <b-field id="form-id-group"
                                label="Filter Id:"
                                label-for="form-id-input">
                            <b-input id="form-id-input"
                                    type="int"
                                    v-model="addFilterForm.filterId"
                                    required
                                    placeholder="Enter Id"></b-input>
                        </b-field>

                        <b-field id="form-name-group"
                                  label=" Filter Name:"
                                  label-for="form-name-input">
                            <b-input id="form-name-input"
                                      type="text"
                                      v-model="addFilterForm.filterName"
                                      required
                                      placeholder="Enter Filter Name">
                            </b-input>
                        </b-field>

                    <button class="button is-primary"  @click="onSubmit">Submit</button>
                    <button class="button is-danger"  @click="onReset" >Reset</button>
                    </section>

                  </form>
                </div>
            </div>
   </b-modal>
    <b-modal :active.sync="isUpdateModalActive" :width="640" scroll="keep">
            <div class="card">
           
                <div class="card-content">
                  <form class="w-100" ref="editFilterModal"
                            id="edit-modal"
                            title="Edit Flter"
                            hide-footer>
                    <section>
                        <b-field id="form--edit-id-group"
                                label="Filter Id:"
                                label-for="form-edit-id-input">
                            <b-input id="form-edit-id-input"
                                    type="int"
                                    v-model="editFilterForm.filterId"
                                    required
                                    placeholder="Enter Id"></b-input>
                        </b-field>

                        <b-field id="form-edit-name-group"
                                  label=" Filter Name:"
                                  label-for="form-edit-name-input">
                            <b-input id="form-edit-name-input"
                                      type="text"
                                      v-model="editFilterForm.filterName"
                                      required
                                      placeholder="Enter Filter Name">
                            </b-input>
                        </b-field>

                    <button class="button is-primary" @click="onSubmitUpdate">Update</button>
                    <button class="button is-danger"  @click="onResetUpdate" >Reset</button>
                    </section>

                  </form>
                </div>
            </div>
   </b-modal>
  </div>
</template>

 

<script>
import axios from 'axios';

export default {
  name: 'Locatons',
  data() {
    return {
      msg: [],
      trigger: '',
      isCardModalActive: false,
      isUpdateModalActive: false,
      addFilterForm: {
        filterId: '',
        filterName: '',
      },
      editFilterForm: {
        filterId: '',
        filterName: '',
      },
    };
  },
  methods: {
    getFilters() {
      const path = 'http://localhost:5000/filters';
      axios.get(path)
        .then((res) => {
          this.msg = res.data.filters;
          console.log(this.msg)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addFilter(payload) {
      const path = 'http://localhost:5000/filters';
      axios.post(path, payload)
        .then(() => {
          this.getFilters();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getFilters();
        });
    },
    initForm() {
      this.addFilterForm.filterId = '';
      this.addFilterForm.filterName = '';
      this.editFilterForm.filterId = '';
      this.editFilterForm.filterName = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.isCardModalActive=false;
      const payload = {
        filterId: this.addFilterForm.filterId,
        filterName: this.addFilterForm.filterName,
      };
      this.addFilter(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
        evt.preventDefault();
        this.isUpdateModalActive=false;
        const payload = {
            filterId: this.editFilterForm.filterId,
            filterName: this.editFilterForm.filterName,
        };
        this.updateFilter(payload, this.editFilterForm.filterId);
        },
    onReset(evt) {
        evt.preventDefault();
        this.initForm();
    },
    onResetUpdate(evt) {
        evt.preventDefault();
        this.isUpdateModalActive=false;
        this.initForm();
        this.getFilters();
    },
    editFilter(filter){
        this.editFilterForm=filter;
    },
    updateFilter(payload, filterId){
        const path = `http://localhost:5000/filters/${filterId}`;
        axios.post(path, payload)
            .then(() => {
            this.getFilters();
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.getFilters();
            });
    },
    onTrigger(event){
        if(event.target.value=== 'add'){
            this.initForm();
        }else if(event.target.value=== 'edit'){
            this.editFilter(event.target.id)
        }
        this.isCardModalActive=true;

    }

  },
  created() {
    this.getFilters();
  },
};
</script>