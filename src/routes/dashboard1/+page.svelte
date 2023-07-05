<script>
	import { fade } from 'svelte/transition';
  import Button2 from "../../components/ui/buttons/IconButton.svelte";
  import Card1Image from "../../components/ui/cards/Card1Image.svelte";
  import Card1People from "../../components/ui/cards/Card1People.svelte";
  import Card1Stat from "../../components/ui/cards/Card1Stat.svelte";
  import Card1Text from "../../components/ui/cards/Card1Text.svelte";
  import Card2Image from "../../components/ui/cards/Card2Image.svelte";
 
</script>

<div  class="px-10 mt-14 absolute inset-0 bg-black z-50 m-0 -mt-10 pt-20">

  
  <div class="grid grid-cols-9 gap-16">
    <div class="col-span-3 flex flex-col space-y-7">
      <Card1Text />
        <h2 class="text-2xl">Staff conected</h2>
        <div class="flex flex-col space-y-3">
            <Card1People />
        
        </div>
    </div>
    <div class="col-span-5 flex flex-col">
      <Card1Image />
  
      <div class="grid gap-3 mt-7 grid-cols-2">
        <Card2Image imageSrc="/b5.jpg" />
        <div class="flex flex-col space-y-3">
          <Card1Stat
            color="bg-sky-500"
            period="2/2023"
            modelValue={1545}
            modelName="Locations"
          />
          <Card1Stat
            color="bg-yellow-500/80"
            period="2/2023"
            modelValue={254}
            modelName="Clients"
          />
        </div>
      </div>
    </div>
    <div class="col-span-1">
      <div class="flex flex-col space-y-7">
        <Button2 icon="data" title="Data" />
        <Button2 icon="newspaper" title="Blog" />
        <Button2 icon="growth" title="Growth" />
      </div>
    </div>
  </div>
</div>
