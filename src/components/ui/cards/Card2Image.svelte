<script lang="ts">
  import { fade, fly } from "svelte/transition";
  import Button1 from "../buttons/Button1.svelte";
  import ButtonLink1 from "../buttons/ButtonLink1.svelte";

  export let imageSrc: String = "/b2.jpg";
</script>

<div
  in:fly={{ y: 150, duration: 3000 }}
  out:fade
  class={`bg-[url('${imageSrc}')] h-56 object-center rounded-3xl p-3`}
>
  <div class="flex justify-between p-6">
    <div class="flex flex-col h-full justify-between">
      <div>
        <ButtonLink1 />

        <p class="text-gray-200 font-semibold shadow-2xl mt-7 text-sm">
          New Place:
        </p>
        <h2 class="text-gray-100 text-2xl font-bold">
          Time to unleassh the Explorer of new
        </h2>
      </div>
    </div>
  </div>
</div>
