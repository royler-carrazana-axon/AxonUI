<script lang="ts">
  import { fly } from "svelte/transition";

  //Props
  export let userName: string = "Royler Marichal";
  export let userImage: string = "/profile1.jpg";
  export let userRole: string = "Support Team";
</script>

<div
  transition:fly={{ x: 15, duration: 3000 }}
  class="w-full rounded-xl space-x-3 bg-gradient-to-br from-slate-500 via-gray-500 to-slate-800 shadow-xl hover:opacity-90 cursor-pointer flex p-2"
>
  <img src={userImage} class="w-14 h-14 rounded-full grow-0" alt="" />
  <div class="flex flex-col">
    <h3 class="font-bold">{userName}</h3>
    <p class="text-gray-200">{userRole}</p>
  </div>
</div>
