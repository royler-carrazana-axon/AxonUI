/** @type {import('tailwindcss').Config} */
export default {
	darkMode: "class",
	content: [
		"./src/**/*.{html,js,svelte,ts}",
		"./stories/**/*.{html,js,svelte,ts}",
	],
	theme: {
		extend: {
			colors: {
				"primary": "var(--primary-color)",
				"secondary-color": "var(--secondary-color)",
			},
		},
	},
	plugins: [],
};
