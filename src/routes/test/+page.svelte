<script lang="ts">
  import { onMount } from "svelte";
  import * as Page from "axonui";
  // Importa los componentes de botón
  import Button1 from "../../components/ui/buttons/Button.svelte";
  import Button2 from "../../components/ui/buttons/IconButton.svelte";
  import type { SvelteComponent } from "svelte";

  let buttons: (typeof Button1 | typeof Button2)[] = []; // Almacena los componentes de botón

  onMount(() => {
    // Agrega los componentes de botón a la matriz
    buttons = [Button1, Button2];
  });

  function copyCode(event: CustomEvent<number>) {
    const index = event.detail;
    const button = buttons[index];

    if (button) {
      const code = button._svelte?.fragment?.component?.toString();
      console.log(code);
      // Aquí puedes realizar las operaciones necesarias con el código del componente
    }
  }
</script>

<main>
  <h1>Button Gallery</h1>
  {Page}
  {#each buttons as button, index}
    <section>
      <h2>{button.$options?.name}</h2>
      <svelte:component
        this={button}
        on:click={() => copyCode({ detail: index })}
      />

      <div>
        <h3>Button Code:</h3>
        {#if button}
          <pre><code>{button._svelte?.fragment?.component?.toString()}</code
            ></pre>
        {/if}
      </div>
    </section>
  {/each}
</main>

<style>
  /* Estilos personalizados para ButtonGallery */
</style>
