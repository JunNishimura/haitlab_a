<template>
    <div class="auth__model">
        <BaseCard>
            <slot name="form"></slot>
            <!-- <div class="line"></div>
            <div class="or">
                <p>OR</p>
            </div>
            <BaseButton class="facebook">
                <span class="btn-title">{{ facebookButtonTitle }}</span>
                <FontAwesomeIcon :icon="['fab', 'facebook-square']" size="lg"/>
            </BaseButton>
            <BaseButton class="twitter" @buttonEvent="twitterSign">
                <span class="btn-title">{{ twitterButtonTitle }}</span>
                <FontAwesomeIcon :icon="['fab', 'twitter-square']" size="lg"/>
            </BaseButton> -->
        </BaseCard>
    </div>
</template>

<script>
export default {
    props: ['mode'],
    computed: {
        facebookButtonTitle() {
            if (this.mode === 'signup') return "Facebookで登録";
            else return 'Facebookでログイン';
        },
        twitterButtonTitle() {
            if (this.mode == 'signup') return 'Twitterで登録';
            else return 'Twitterでログイン';
        }
    },
    methods: {
        twitterSign() {
            this.$store.dispatch("auth/twitterSign");
        }
    }
}
</script>

<style lang="scss" scoped>
.auth__model {
    padding: 2rem 0;
}

.card {
    max-width: 30rem;
    padding: 2rem;
}

.line {
    padding: 1rem 0;
    border-bottom: 1px solid #000000;
}

.or {
    text-align: center;
    margin-top: -30px;
}

.btn-title {
    margin-right: 1rem;
}

.facebook {
    color: #eeeeee;
    background-color: #3A559F;
    margin-bottom: .5rem;
    
    &:hover {
        transition: all .25s ease-in;
        background-color: #163896;
    }
}

.twitter {
    color: #eeeeee;
    background-color: #50ABF1;
    
    &:hover {
        transition: all .25s ease-in;
        background-color: #3297e4;
    }
}
</style>