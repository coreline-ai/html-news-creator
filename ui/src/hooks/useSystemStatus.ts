import {
  useMutation,
  useQuery,
  useQueryClient,
  type UseMutationResult,
  type UseQueryResult,
} from "@tanstack/react-query";
import {
  apiFetch,
  type ProxyRecoveryResponse,
  type SystemStatusResponse,
} from "@/lib/api";

/** GET /api/system/status — local runtime dependency status. */
export function useSystemStatus(): UseQueryResult<SystemStatusResponse, Error> {
  return useQuery<SystemStatusResponse, Error>({
    queryKey: ["system-status"],
    queryFn: () => apiFetch<SystemStatusResponse>("/api/system/status"),
    retry: false,
    staleTime: 5_000,
    refetchInterval: 10_000,
  });
}

/** POST /api/system/proxy/recover — best-effort local proxy recovery. */
export function useRecoverProxy(): UseMutationResult<
  ProxyRecoveryResponse,
  Error,
  void
> {
  const queryClient = useQueryClient();
  return useMutation<ProxyRecoveryResponse, Error, void>({
    mutationFn: () =>
      apiFetch<ProxyRecoveryResponse>("/api/system/proxy/recover", {
        method: "POST",
        body: "{}",
      }),
    onSuccess: () => {
      void queryClient.invalidateQueries({ queryKey: ["system-status"] });
    },
  });
}
