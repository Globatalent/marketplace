<template>
  <div>
    <div v-if="imageUrl" class="text-center">
      <img :src="imageUrl" alt="" class="preview m-b-10">
      <el-button type="danger" class="is-uppercase" @click.prevent="deleteImage()">{{ $tc('message.DeleteImage') }}
      </el-button>
    </div>
    <form v-else
          :class="['box', {'has-advanced-upload': dragAndDropCapable, 'is-error': hasError}]"
          method="post" action="" ref="fileform"
          enctype="multipart/form-data">
      <div class="box__input">
        <input class="box__file" type="file" name="files[]" id="file" @change="uploadFile($event)"/>
        <label for="file">
          <i class="el-icon-upload" style="padding: 0"></i>
          <strong>Choose a file</strong><span class="box__dragndrop"> or drag it here</span>.
          <el-progress :text-inside="true" :stroke-width="18" :percentage="uploadPercentage"
                       v-if="uploading" class="m-t-10"></el-progress>
        </label>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'ImageUpload',
    props: {
      fieldName: {
        type: String
      },
      campaignId: {
        type: Number
      },
      imageUrl: {
        type: String
      }
    },
    data () {
      return {
        uploadPercentage: 0,
        dragAndDropCapable: false,
        file: null,
        uploading: false,
        hasError: false
      }
    },
    methods: {
      determineDragAndDropCapable () {
        const div = document.createElement('div')
        return (('draggable' in div)
          || ('ondragstart' in div && 'ondrop' in div))
          && 'FormData' in window
          && 'FileReader' in window
      },
      removeFile (key) {
        this.files.splice(key, 1)
      },
      deleteImage () {
        let formData = new FormData()
        formData.append(this.fieldName, [])
        this.sendRequest(formData)
      },
      submitFile () {
        let formData = new FormData()

        formData.append(this.fieldName, this.file)
        this.sendRequest(formData)
      },
      sendRequest (data) {
        this.uploadPercentage = 0
        this.uploading = true
        this.axios.patch(`${this.$store.state.campaigns.endpoints.campaigns}${this.campaignId}/`,
          data,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            },
            onUploadProgress: progressEvent => {
              this.uploadPercentage = parseInt(Math.round((progressEvent.loaded * 100) / progressEvent.total))
            }
          }
        ).then(({data}) => {
          this.$emit('image-changed', this.fieldName, data[this.fieldName])
          this.uploading = false
        }).catch((error) => {
          console.log('FAILURE!!')
          console.log(error)
          this.uploading = false
        })
      },
      uploadFile (e) {
        this.file = e.target.files[0]
        this.submitFile()
      }
    },
    mounted () {

      const vm = this
      this.dragAndDropCapable = this.determineDragAndDropCapable()
      if (this.dragAndDropCapable) {
        ['drag', 'dragstart', 'dragend', 'dragover', 'dragenter', 'dragleave', 'drop'].forEach(evt => {
          vm.$refs.fileform.addEventListener(evt, e => {
            e.preventDefault()
            e.stopPropagation()
          })
        });

        ['dragover', 'dragenter'].forEach(evt => {
          vm.$refs.fileform.addEventListener(evt, e => {
            vm.$refs.fileform.classList.add('is-dragover')
          })
        });

        ['dragleave', 'dragend', 'drop'].forEach(evt => {
          vm.$refs.fileform.addEventListener(evt, e => {
            vm.$refs.fileform.classList.remove('is-dragover')
          })
        })

        vm.$refs.fileform.addEventListener('drop', function (e) {
          vm.file = e.dataTransfer.files[0]
          vm.submitFile()
        }.bind(this))

        vm.$refs.fileform.addEventListener('drop', function (e) {
          vm.file = e.dataTransfer.files[0]
          vm.submitFile()
        }.bind(this))
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import '@/scss/variables.scss';

  .box.has-advanced-upload {
    background-color: $--grey-detailCampaign-box;
    border: 1px dashed $--grey-detailCampaign-border;
    /* outline-offset: -10px; */
    height: 200px;
    position: relative;
    border-radius: $--border-radius-base;
    .box__dragndrop {
      display: inline;
    }
    input, .box__button {
      display: none
    }
    .box__input label {
      text-align: center;
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      padding: 30px;
      cursor: pointer;
    }
  }

  .box.is-dragover {
    background-color: grey;
  }

  .box.is-uploading .box__input {
    display: none;
  }

  .box.is-uploading .box__uploading {
    display: block;
  }

  .preview {
    width: 200px;
    height: 200px;
    display: block;
    margin: 10px auto;
  }

  .el-icon-upload {
    font-size: 4rem;
    color: $--grey;
    display: block;
    margin: 10px auto;
  }
</style>
