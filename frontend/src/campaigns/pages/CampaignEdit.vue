<template>
  <gb-base-layout>
    <div class="athleteProfileEdit">
      <h2 class="form-lined-title">{{ $tc("message.AthleteProfileEditPage") }}</h2>
      <div class="form-lined">
        <el-row :gutter="20" type="flex">
          <el-col :xs="24" :sm="16" class="form-lined-column">
            <el-form ref="form" :model="form" :rules="rules">
              <el-row justify="center" :gutter="20">
                <el-col :xs="24" :sm="12" :md="12" class="text-center">
                  <el-form-item required prop="firstName">
                    <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
                  </el-form-item>
                  <el-form-item required prop="lastName">
                    <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
                  </el-form-item>
                  <el-form-item required prop="birthDate">
                    <el-date-picker type="date" v-bind:placeholder="$tc('message.DateOfBirth')" style="width: 100%;" v-model="form.birthDate"></el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" class="text-center">
                  <el-form-item required prop="country">
                    <el-input v-bind:placeholder="$tc('message.Country')" type="text" v-model="form.country"></el-input>
                  </el-form-item>
                  <el-form-item required prop="sport">
                    <el-input v-bind:placeholder="$tc('message.Sport')" type="text" v-model="form.sport"></el-input>
                  </el-form-item>
                  <el-form-item v-bind:label="$tc('message.Sex')" class="text-left sexFormElement" prop="sex">
                    <el-radio-group v-model="form.sex">
                      <el-radio label="MALE">{{ $tc("message.Male") }}</el-radio>
                      <el-radio label="FEMALE">{{ $tc("message.Female") }}</el-radio>
                    </el-radio-group>
                  </el-form-item>
                </el-col>
              </el-row>
              <h3 class="form-lined-sectionTitle text-center">{{$tc('message.Link',2)}}</h3>
              <el-row type="flex" justify="left" :gutter="20" v-for="(link, index) in links" :key="index">
                <el-col :xs="24" :sm="12" :md="12" class="text-center">
                  <el-form-item prop="linkName">
                    <el-input v-bind:placeholder="$tc('message.LinkTitle')" type="text" v-model="link.name"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="11" :md="11" class="text-center">
                  <el-form-item prop="linkUrl">
                    <el-input v-bind:placeholder="$tc('message.Link')" type="text" v-model="link.url"></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="1" :md="1" class="text-left removeButtonCol">
                  <div @click="deleteRow(index)" class="circleButton">
                    <i class="fa fa-minus-circle addButtonCircle"></i>
                  </div>
                </el-col>
              </el-row>
              <el-row type="flex" justify="center" :gutter="20" class="linksRow">
                <el-col :xs="24" class="text-center">
                  <el-button type="primary" class="is-uppercase" @click="addRow">{{ $tc("message.addLink") }}</el-button>
                </el-col>
              </el-row>
              <h3 class="form-lined-sectionTitle text-center">{{ $tc("message.AthleteImage") }}</h3>
              <el-row type="flex" justify="center" :gutter="20">
                <el-col :xs="24" :sm="18" :md="18" class="text-center">
                  <vue-dropzone ref="picturesDropzone" id="dropzone" :options="dropzoneOptions" @vdropzone-removed-file="vdropzoneRemoved"></vue-dropzone>
                </el-col>
              </el-row>
              <el-row type="flex" justify="center" :gutter="20">
                <el-col :xs="24" class="text-center">
                  <el-form-item class="text-center">
                    <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc("message.Save") }}</el-button>
                  </el-form-item>
                </el-col>
              </el-row>
            </el-form>
          </el-col>
          <el-col :xs="24" :sm="8">
            <el-form ref="formSale" :model="formSale" :rules="rulesSale">
              <el-form-item required prop="name">
                <el-input v-bind:placeholder="$tc('message.TokenName')" type="text" v-model="formSale.name" :disabled="isSaleCreated"></el-input>
              </el-form-item>
              <el-form-item required prop="code">
                <el-input v-bind:placeholder="$tc('message.TokenCode')" type="text" v-model="formSale.code" :disabled="isSaleCreated"></el-input>
              </el-form-item>
              <el-form-item required prop="amount">
                <el-input v-bind:placeholder="$tc('message.Quantity')" type="number" v-model="formSale.amount" :disabled="isSaleCreated"></el-input>
              </el-form-item>
              <el-form-item required prop="price">
                <el-input v-bind:placeholder="$tc('message.TotalPrice')" type="number" v-model="formSale.price" :disabled="isSaleCreated"></el-input>
              </el-form-item>
              <el-row type="flex" justify="center" :gutter="20">
                <el-col :xs="24" class="text-center">
                  <el-form-item class="text-center">
                    <el-button type="primary" class="is-uppercase" @click.prevent="onSubmitToken('formSale')">{{ $tc("message.SaveSale") }}</el-button>
                  </el-form-item>
                </el-col>
              </el-row>
            </el-form>
          </el-col>
        </el-row>

      </div>
    </div>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
import BaseLayout from '@/layout/BaseLayout.vue'
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { mapGetters } from 'vuex'

export default {
  name: 'CampaignForm',
  components: {
    'gb-base-layout': BaseLayout,
    vueDropzone: vue2Dropzone
  },
  computed: {
    ...mapGetters({
      user: 'users/user'
    })
  },
  data() {
    return {
      isSaleCreated: false,
      form: {},
      formSale: {},
      links: [],
      linksToDelete: [],
      pictures: [],
      picturesToDelete: [],
      // vue-dropzone Docs  https://rowanwins.github.io/vue-dropzone/docs/dist/#/manual
      dropzoneOptions: {
        url: `${Vue.axios.defaults.baseURL}/api/v1/pictures/`,
        paramName: 'image',
        thumbnailWidth: 150,
        maxFilesize: 2,
        addRemoveLinks: true,
        headers: {
          Authorization: this.$store.getters['auth/header']
        }
      },
      rules: {
        firstName: [
          {
            required: true,
            message: 'Please input first name',
            trigger: 'blur'
          }
        ],
        lastName: [
          { required: true, message: 'Please input last name', trigger: 'blur' }
        ],
        birthDate: [
          {
            required: true,
            message: 'Please input birth date',
            trigger: 'blur'
          }
        ],
        country: [
          { required: true, message: 'Please input country', trigger: 'blur' }
        ],
        sport: [
          { required: true, message: 'Please input sport', trigger: 'blur' }
        ]
      },
      rulesSale: {
        name: [
          {
            required: true,
            message: 'Please input token name',
            trigger: 'blur'
          }
        ],
        code: [
          {
            required: true,
            message: 'Please input token code',
            trigger: 'blur'
          }
        ],
        amount: [
          {
            validator: this.validateQuantity,
            trigger: 'blur'
          }
        ],
        price: [
          {
            required: true,
            message: 'Please input total price',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  created() {
    this.$store
      .dispatch('users/fetchUser')
      .then(() => {
        this.form = { ...this.user.athlete }
        this.links = this.user.athlete.links
        this.pictures = this.user.athlete.pictures
        if (this.links.length == 0) {
          this.addRow()
        }
        this.loadPictures()
        this.isSaleCreated = !!this.user.athlete.token
        if (this.isSaleCreated) {
          this.formSale = { ...this.user.athlete.token }
        }
      })
      .catch(error => {
        console.log(error)
      })
  },
  methods: {
    vdropzoneRemoved(file, xhr, error) {
      if (this.$children[0]._isBeingDestroyed) { return }
      const images = this.pictures.filter(picture => picture.id === file.id)
      if (images.length > 0) {
        this.$store.dispatch('athletes/deletePicture', images[0])
      }
    },
    loadPictures() {
      this.pictures.forEach(picture => {
        const url = picture.image
        const name = url.substring(url.lastIndexOf('/') + 1)
        const file = { size: 123, name: name, id: picture.id }
        this.$refs.picturesDropzone.manuallyAddFile(file, url)
      })
    },
    validateQuantity(rule, value, callback) {
      if (value === '' || !value) {
        callback(new Error('Please input the quantity'))
      } else {
        const n = Math.floor(Number(value))
        let isInteger = n !== Infinity && String(n) === value && n >= 0
        if (!isInteger) {
          callback(new Error('Please input positive integer'))
        } else {
          callback()
        }
      }
    },
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = Object.assign({}, this.form)
          this.saveUserProfile(dataForm)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    saveUserProfile(data) {
      const linksToCreate = this.links.filter(link => !link.id && !!link.name)
      const linksToUpdate = this.links.filter(link => !!link.id)
      const payload = {
        linksToCreate: linksToCreate,
        linksToUpdate: linksToUpdate,
        linksToDelete: this.linksToDelete,
        ...data
      }
      this.$store
        .dispatch('athletes/update', data)
        .then(response => {
          Promise.all(
            linksToCreate
              .map(link => {
                return this.$store.dispatch('athletes/createLink', link)
              })
              .concat(
                linksToUpdate.map(link => {
                  return this.$store.dispatch('athletes/updateLink', link)
                })
              )
              .concat(
                this.linksToDelete.map(link => {
                  return this.$store.dispatch('athletes/deleteLink', link)
                })
              )
              .then(() => {
                console.log('Links saved!')
              })
              .catch(() => {
                console.error('Error saving links!')
              })
          )
        })
        .catch(error => {})
    },
    addRow() {
      this.links.push({ name: '', url: '' })
    },
    deleteRow(index) {
      const link = this.links[index]
      if (!!link.id) {
        this.linksToDelete.push(link)
      }
      this.links.splice(index, 1)
    },
    onSubmitToken(form) {
      this.$refs[form].validate(valid => {
        if (valid && !this.isSaleCreated) {
          const tokenData = { ...this.formSale }
          this.$store.dispatch('tokens/create', tokenData).then(response => {
            this.isSaleCreated = true
          }).catch(error => {
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
  }
}
</script>

<style scoped>
</style>
