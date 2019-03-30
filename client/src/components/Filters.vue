<template>
  <div class="conatiner">
    <div class="columns">
      <div class="column is-half">
        <div class="card">
          <div class="card-content">
            <form
              class="w-100"
              ref="addFilterModal"
              id="add-modal"
              title="Add a new filter"
              hide-footer
            >
              <section>
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <b-field label="Filter Id" label-for="filter-id"/>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <b-input
                          v-model="addFilterForm.filterId"
                          id="filter-id"
                          type="text"
                          required
                          placeholder="Enter Filter Id"
                        ></b-input>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <b-field label="Filter Name" label-for="filter-name"/>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <b-input
                          v-model="addFilterForm.filterName"
                          id="filter-name"
                          type="text"
                          required
                          placeholder="Enter Filter Name"
                        ></b-input>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="field-body">
                  <div style="padding:5px" class="field">
                    <button class="button is-primary is-pulled-right" @click="onSubmit">Submit</button>
                    <!-- <button class="button is-danger" @click="onReset">Reset</button> -->
                  </div>
                </div>
              </section>
            </form>
          </div>
        </div>
      </div>
      <div class="column is-half">
        <div class="card">
          <div class="card-content">
            <div class="title is-4">Current Food Items</div>
            <b-table :data="data">
              <template slot-scope="props">
                <b-table-column field="filterId" label="Item Id" width="40">{{ props.row.filterId }}</b-table-column>
                <b-table-column
                  field="filterName"
                  label="Name"
                  width="40"
                >{{ props.row.filterName }}</b-table-column>
                <b-table-column label="Delete" width="40">
                  <button
                    type="button"
                    class="button"
                    @click="deleteFilter( props.row.filterId)"
                  >Delete</button>
                </b-table-column>
                <b-table-column label="Update" width="40">
                  <button
                    type="button"
                    value="edit"
                    class="button"
                    @click="editFilter(props.row),isUpdateModalActive = true"
                  >Update</button>
                </b-table-column>
              </template>
            </b-table>
          </div>
        </div>
      </div>
    </div>

    <b-modal :active.sync="isUpdateModalActive" :width="640" scroll="keep">
      <div class="card">
        <div class="card-content">
          <form class="w-100" ref="editFilterModal" id="edit-modal" title="Edit Flter" hide-footer>
            <section>
              <b-field id="form--edit-id-group" label="Filter Id:" label-for="form-edit-id-input">
                <b-input
                disabled
                  id="form-edit-id-input"
                  type="int"
                  v-model="editFilterForm.filterId"
                  required
                  placeholder="Enter Id"
                ></b-input>
              </b-field>

              <b-field
                id="form-edit-name-group"
                label=" Filter Name:"
                label-for="form-edit-name-input"
              >
                <b-input
                  id="form-edit-name-input"
                  type="text"
                  v-model="editFilterForm.filterName"
                  required
                  placeholder="Enter Filter Name"
                ></b-input>
              </b-field>

              <button class="button is-primary" @click="onSubmitUpdate">Update</button>
              <button class="button is-danger" @click="onResetUpdate">Reset</button>
            </section>
          </form>
        </div>
      </div>
    </b-modal>
  </div>
</template>

 

<script>
import axios from "axios";

export default {
  name: "Locatons",
  data() {
    return {
      data: [],
      trigger: "",
      isUpdateModalActive: false,
      addFilterForm: {
        filterId: "",
        filterName: ""
      },
      editFilterForm: {
        filterId: "",
        filterName: ""
      }
    };
  },
  methods: {
    getFilters() {
      const path = "http://localhost:5000/filters";
      axios
        .get(path)
        .then(res => {
          this.data = res.data.filters;
          console.log(this.data);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addFilter(payload) {
      const path = "http://localhost:5000/filters";
      axios({
        method: "post",
        url: "http://localhost:5000/filters",
        data: {
          filterId: payload.filterId,
          filterName: payload.filterName
        }
      })
        .then(function(response) {
          this.getFilters();
        })
        .catch(function(error) {});
    },
    deleteFilter(id) {
      const path = `http://localhost:5000/filters/${id}`;
      axios
        .delete(path)
        .then(() => {
          this.getFilters();
        })
        .catch(error => {
          this.getFilters();
        });
    },
    initForm() {
      this.addFilterForm.filterId = "";
      this.addFilterForm.filterName = "";
      this.editFilterForm.filterId = "";
      this.editFilterForm.filterName = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.isCardModalActive = false;
      const payload = {
        filterId: this.addFilterForm.filterId,
        filterName: this.addFilterForm.filterName
      };
      this.addFilter(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.isUpdateModalActive = false;
      const payload = {
        filterId: this.editFilterForm.filterId,
        filterName: this.editFilterForm.filterName
      };
      this.updateFilter(payload, this.editFilterForm.filterId);
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.isUpdateModalActive = false;
      this.initForm();
      this.getFilters();
    },
    editFilter(filter) {
      this.editFilterForm = filter;
    },
    updateFilter(payload, filterId) {
      const path = `http://localhost:5000/filters/${filterId}`;
      axios
        .post(path, payload)
        .then(() => {})
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onTrigger(event) {
      if (event.target.value === "add") {
        this.initForm();
      } else if (event.target.value === "edit") {
        this.editFilter(event.target.id);
      }
    }
  },
  created() {
    this.getFilters();
  },
  mounted() {
    this.getFilters();
  }
};
</script>