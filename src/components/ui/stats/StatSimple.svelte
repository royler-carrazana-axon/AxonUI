<script lang="ts">
    import { fade, fly } from "svelte/transition";
  import ButtonLink1 from "../buttons/ButtonLink1.svelte";

  //Params
  export let color: String = "sky";
  export let period: String = "Today";
  export let modelValue: Number = 333;
  export let modelName: String = "Users";
  
</script>
<div>
    <div class="grid grid-cols-2 bg-black">
        <div>
            <div
            in:fly={{ y: 150, duration: 3000 }}
            out:fade
            class={` ${color}  h-auto  object-center rounded-3xl px-3`}
          >
            <div class="flex py-6">
              <ButtonLink1 />
              <div class="flex flex-col w-full pr-7 space-y-1">
                <p
                  class="text-gray-200 ml-auto font-semibold text-right shadow-2xl text-sm"
                >
                  {period}
                </p>
                <h2 class="text-gray-100 text-2xl font-bold self-end text-left">
                  + {modelValue}
                  {modelName}
                </h2>
              </div>
            </div>
          </div>
          
        </div>
        <div>
            <div
            in:fly={{ y: 150, duration: 3000 }}
            out:fade
            class={` ${color}  h-auto  object-center rounded-3xl px-3`}
          >
            <div class="flex py-6">
              <ButtonLink1 />
              <div class="flex flex-col w-full pr-7 space-y-1">
                <p
                  class="text-gray-200 ml-auto font-semibold text-right shadow-2xl text-sm"
                >
                  {period}
                </p>
                <h2 class="text-gray-100 text-2xl font-bold self-end text-left">
                  + {modelValue}
                  {modelName}
                </h2>
              </div>
            </div>
          </div>
          
        </div>
      
    </div>
</div>

