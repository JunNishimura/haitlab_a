<template>
    <div id="post__ideas-page" v-if="loadComplete">
        <div class="post__ideas">
            <IdeaElement
                v-for="idea in postIdeas"
                :key="idea.idea_id"
                :idea_id="idea.idea_id"
                :user_id="idea.user_id"
                :title="idea.title"
                :overview="idea.overview"
                :background="idea.background"
                :passion="idea.passion"
                :idea_img="idea.idea_img"
                :idea_date="idea.idea_date"
            ></IdeaElement>
        </div>
    </div>
</template>

<script>
import apiHelper from '@/services/apiHelper.js';
import IdeaElement from '@/components/Idea/IdeaElement.vue';

export default {
    components: {
        IdeaElement,
    },
    data() {
        return {
            postIdeas: [],
            isMyProfile: false,
            loadComplete: false,
        }
    },
    computed: {
        myUserId() {
            return this.$store.getters['auth/userId'];
        }
    },
    created() {
        // 自分のプロフィールかを確認
        const paramUserId = this.$route.params['userId'];
        if (paramUserId == this.myUserId) {
            this.isMyProfile = true;
        }

        apiHelper.loadFilteredPostIdeas(paramUserId)
        .then( res => {
            this.postIdeas = res;
            this.loadComplete = true;
        }).catch( err => {
            console.log("error to get ideas at PostIdeasPage: ", err);
        })
    }
}
</script>

<style scoped>
.post__ideas .idea {
    margin: 1rem auto;;
}
</style>