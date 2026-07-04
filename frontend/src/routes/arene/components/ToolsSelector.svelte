<script lang="ts">
  import { Button, Icon, Modal } from '$components/dsfr'
  import Selector from '$components/Selector.svelte'
  import { api } from '$lib/fastapi-client'
  import { m } from '$lib/i18n/messages'
  import { onMount } from 'svelte'

  interface LegalToolOption {
    id: string
    label: string
    description: string
  }

  let {
    enabledSkills = $bindable([]),
    enabledMcpServers = $bindable([])
  }: {
    enabledSkills: string[]
    enabledMcpServers: string[]
  } = $props()

  let skills = $state<LegalToolOption[]>([])
  let mcpServers = $state<LegalToolOption[]>([])

  onMount(async () => {
    try {
      const data = await api.request<{ skills: LegalToolOption[]; mcp_servers: LegalToolOption[] }>(
        '/arena/legal_tools'
      )
      skills = data.skills
      mcpServers = data.mcp_servers
    } catch (e) {
      console.error('[ToolsSelector] Failed to load legal tools', e)
    }
  })

  const selectedCount = $derived(enabledSkills.length + enabledMcpServers.length)

  function closeModal() {
    // @ts-expect-error - DSFR is globally available
    window.dsfr(document.getElementById('modal-tools-selector'))?.modal.conceal()
  }
</script>

{#if skills.length || mcpServers.length}
  <Button
    variant="secondary"
    native
    aria-controls="modal-tools-selector"
    data-fr-opened="false"
    class="bg-white! px-3! text-sm! text-dark-grey! md:w-auto! w-full! items-center justify-start"
    style="--border-action-high-blue-france: var(--grey-925-125)"
  >
    <Icon icon="i-ri-tools-fill" block size="sm" class="text-primary me-2" />
    <span class="label">
      {m['arenaHome.legalTools.legend']()}
      {#if selectedCount}
        · {selectedCount}
      {/if}
    </span>
    <Icon icon="i-ri-arrow-down-s-line" block size="sm" class="md:ms-2 ms-auto" />
  </Button>

  <Modal
    id="modal-tools-selector"
    titleId="modal-tools-selector-title"
    sizeClass="fr-col-12 fr-col-md-8 fr-col-lg-6"
    onClose={closeModal}
  >
    <h6 id="modal-tools-selector-title" class="mb-3!">
      {m['arenaHome.legalTools.legend']()}
    </h6>

    <div class="flex flex-col gap-4">
      {#if mcpServers.length}
        <div>
          <p class="mb-2! text-xs font-medium text-dark-grey">
            {m['arenaHome.legalTools.mcpServers.legend']()}
          </p>
          <Selector
            id="enabled-mcp-servers"
            kind="checkbox"
            multiple
            bind:value={enabledMcpServers}
            choices={mcpServers.map((s) => ({ value: s.id, label: s.label }))}
            containerClass="flex flex-wrap gap-2"
            choiceClass="text-sm px-3 py-2 rounded-full! flex items-center gap-1.5 cursor-pointer"
          >
            {#snippet option(opt, labelProps, input)}
              {@const server = mcpServers.find((s) => s.id === opt.value)}
              <label {...labelProps} title={server?.description}>
                {@render input(opt)}
                <Icon icon="i-ri-tools-fill" size="sm" />
                {opt.label}
              </label>
            {/snippet}
          </Selector>
        </div>
      {/if}

      {#if skills.length}
        <div>
          <p class="mb-2! text-xs font-medium text-dark-grey">
            {m['arenaHome.legalTools.skills.legend']()}
          </p>
          <Selector
            id="enabled-skills"
            kind="checkbox"
            multiple
            bind:value={enabledSkills}
            choices={skills.map((s) => ({ value: s.id, label: s.label }))}
            containerClass="flex flex-wrap gap-2"
            choiceClass="text-sm px-3 py-2 rounded-full! flex items-center gap-1.5 cursor-pointer"
          >
            {#snippet option(opt, labelProps, input)}
              {@const skill = skills.find((s) => s.id === opt.value)}
              <label {...labelProps} title={skill?.description}>
                {@render input(opt)}
                <Icon icon="i-ri-sparkling-2-fill" size="sm" />
                {opt.label}
              </label>
            {/snippet}
          </Selector>
        </div>
      {/if}

      <p class="mb-0! text-xs text-dark-grey">
        {m['arenaHome.legalTools.help']()}
      </p>
    </div>
  </Modal>
{/if}
