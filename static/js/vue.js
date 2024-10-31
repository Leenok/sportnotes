const { createApp, ref } = Vue;
console.log("vue");
createApp({
	setup() {
		const message = ref("Hello Vue!");
		return {
			message,
		};
	},
}).mount("#app");
